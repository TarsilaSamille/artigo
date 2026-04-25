import asyncio
import os
from playwright.async_api import async_playwright

OUT = os.path.dirname(os.path.abspath(__file__))

async def capture_v4_v3():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        # 1000px width - slightly wider but still great for print text scale
        context = await browser.new_context(
            viewport={"width": 1000, "height": 3000},
            device_scale_factor=2.0
        )
        page = await context.new_page()
        page.set_default_timeout(120000)

        print("1. Loading V4 Pipeline (V3 Robust - 1000px Viewport)...")
        await page.goto("https://bidayuhjagoy.vercel.app/", wait_until="networkidle")
        
        # Translate
        await page.locator("textarea").first.fill("tell these stones to become bread")
        await page.locator("#translateBtn").click()
        await page.wait_for_selector("#translateBtn:not(:has-text('Send'))", timeout=120000)
        await page.wait_for_timeout(5000) 

        # Capture A: Main UI
        print("   Capturing main UI...")
        # Get bounding box of the formal card
        await page.evaluate("window.scrollTo(0, 0)")
        await page.screenshot(path=f"{OUT}/fig_main_v4.png", clip={"x": 5, "y": 80, "width": 990, "height": 700})

        # Expand Analysis and Debug
        print("   Expanding Trace...")
        await page.evaluate('''() => {
            const panel = document.querySelector('#sentenceDetailPanel');
            if (panel) panel.classList.remove('hidden');
            const summary = [...document.querySelectorAll('summary')].find(s => s.innerText.includes('Full Prompt'));
            if (summary) summary.click();
        }''')
        await page.wait_for_timeout(3000)

        # Capture B: Analysis
        print("   Capturing analysis...")
        await page.screenshot(path=f"{OUT}/fig_analysis_v4.png", clip={"x": 5, "y": 800, "width": 990, "height": 800})

        # Capture C: Debug
        print("   Capturing debug JSON...")
        await page.screenshot(path=f"{OUT}/fig_debug_v4.png", clip={"x": 5, "y": 1600, "width": 990, "height": 1000})

        print("   V4 Focusing Assets (V3) Generated!")
        await browser.close()

if __name__ == "__main__":
    asyncio.run(capture_v4_v3())
