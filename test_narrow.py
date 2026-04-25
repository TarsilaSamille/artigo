import asyncio
import os
from playwright.async_api import async_playwright

OUT = os.path.dirname(os.path.abspath(__file__))

async def test_narrow_layout():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        # Use a narrow viewport to force larger text/stacking
        context = await browser.new_context(
            viewport={"width": 640, "height": 1000},
            device_scale_factor=2.0
        )
        page = await context.new_page()
        await page.goto("https://bidayuhjagoy.vercel.app/", wait_until="networkidle")
        
        await page.locator("textarea").first.fill("tell these stones to become bread")
        await page.locator("#translateBtn").click()
        await page.wait_for_selector("text=batuh-batuh", timeout=120000)
        await page.wait_for_timeout(3000)
        
        # Expand debug
        await page.evaluate('''() => {
            const summary = [...document.querySelectorAll('summary')].find(s => s.innerText.includes('Full Prompt'));
            if (summary) summary.click();
            const panel = document.querySelector('#sentenceDetailPanel');
            if (panel) panel.classList.remove('hidden');
        }''')
        await page.wait_for_timeout(2000)

        # Capture with narrow viewport - this usually looks much more 'reasonable' in papers
        # Main UI
        await page.locator("div.formal-card:has(#translateBtn)").first.screenshot(path=f"{OUT}/test_narrow_ui.png")
        # Analysis
        await page.locator("#sentenceDetailPanel").first.screenshot(path=f"{OUT}/test_narrow_analysis.png")
        
        await browser.close()
        print("Narrow UI screenshots generated for evaluation.")

if __name__ == "__main__":
    asyncio.run(test_narrow_layout())
