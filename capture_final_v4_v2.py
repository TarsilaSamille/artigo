import asyncio
import os
from playwright.async_api import async_playwright

OUT = os.path.dirname(os.path.abspath(__file__))

async def capture_final_v4_v2():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        # 720px width - the 'Sweet Spot' for technical paper figures
        context = await browser.new_context(
            viewport={"width": 720, "height": 2000},
            device_scale_factor=2.0
        )
        page = await context.new_page()
        page.set_default_timeout(120000)

        print("1. Loading V4 Pipeline (Focused 720px Viewport - V2 Robust)...")
        await page.goto("https://bidayuhjagoy.vercel.app/", wait_until="networkidle")
        
        # Translate Bible-based Example
        await page.locator("textarea").first.fill("tell these stones to become bread")
        await page.locator("#translateBtn").click()
        print("   Waiting for 'Translate' button to reset...")
        # Wait until button doesn't contain 'sending' or 'translating'
        await page.wait_for_selector("#translateBtn:not(:has-text('Send'))", timeout=120000)
        await page.wait_for_timeout(5000) 

        # Capture A: Translator Interface
        print("   Capturing fig_main_v4.png...")
        # Target the formal-card containing the translate button
        await page.locator("div.formal-card:has(#translateBtn)").first.screenshot(path=f"{OUT}/fig_main_v4.png")

        # Capture B: Analysis Card
        print("   Capturing fig_analysis_v4.png...")
        # Expand analysis visibility
        await page.evaluate('''() => {
            const panel = document.querySelector('#sentenceDetailPanel');
            if (panel) panel.classList.remove('hidden');
        }''')
        analysis_locator = page.locator("#sentenceDetailPanel").first
        await analysis_locator.screenshot(path=f"{OUT}/fig_analysis_v4.png")

        # Capture C: Debug Trace (Expanded)
        print("   Expanding and capturing fig_debug_v4.png...")
        await page.evaluate('''() => {
            const summary = [...document.querySelectorAll('summary')].find(s => s.innerText.includes('Full Prompt'));
            if (summary) summary.click();
        }''')
        await page.wait_for_timeout(3000)
        
        # Capture the whole sentenceDetailPanel area for the debug shot
        # to ensure it captures the expanded content correctly.
        debug_area = await page.locator("#sentenceDetailPanel").first
        await debug_area.screenshot(path=f"{OUT}/fig_debug_v4.png")

        print("   V4 Focusing Assets Generated successfully!")
        await browser.close()

if __name__ == "__main__":
    asyncio.run(capture_final_v4_v2())
