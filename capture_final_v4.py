import asyncio
import os
from playwright.async_api import async_playwright

OUT = os.path.dirname(os.path.abspath(__file__))

async def capture_final_v4():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        # 720px width - the 'Sweet Spot' for technical paper figures
        context = await browser.new_context(
            viewport={"width": 720, "height": 1400},
            device_scale_factor=2.0
        )
        page = await context.new_page()
        page.set_default_timeout(120000)

        print("1. Loading V4 Pipeline (Focused 720px Viewport)...")
        await page.goto("https://bidayuhjagoy.vercel.app/", wait_until="networkidle")
        
        # Translate Bible-based Example
        await page.locator("textarea").first.fill("tell these stones to become bread")
        await page.locator("#translateBtn").click()
        print("   Synthesizing analysis results...")
        await page.wait_for_selector("text=batuh-batuh", timeout=120000)
        await page.wait_for_timeout(4000) 

        # Capture A: Translator Interface
        print("   Capturing fig_main_v4.png...")
        card = await page.locator("div.formal-card:has(#translateBtn)").first
        await card.scroll_into_view_if_needed()
        await card.screenshot(path=f"{OUT}/fig_main_v4.png")

        # Capture B: Analysis Card
        print("   Capturing fig_analysis_v4.png...")
        # Ensure analysis is expanded/visible
        await page.evaluate('''() => {
            const panel = document.querySelector('#sentenceDetailPanel');
            if (panel) panel.classList.remove('hidden');
        }''')
        analysis = await page.locator("#sentenceDetailPanel").first
        await analysis.scroll_into_view_if_needed()
        await analysis.screenshot(path=f"{OUT}/fig_analysis_v4.png")

        # Capture C: Debug Trace (Expanded)
        print("   Expanding and capturing fig_debug_v4.png...")
        await page.evaluate('''() => {
            const summary = [...document.querySelectorAll('summary')].find(s => s.innerText.includes('Full Prompt'));
            if (summary) summary.click();
        }''')
        await page.wait_for_timeout(2000)
        debug_trace = await page.locator("#sentenceDetailPanel details[open] pre").first
        if await debug_trace.count() > 0:
            await debug_trace.screenshot(path=f"{OUT}/fig_debug_v4.png")
        else:
            # Fallback to general area screenshot
            await page.screenshot(path=f"{OUT}/fig_debug_v4.png", clip={"x": 5, "y": 800, "width": 710, "height": 600})

        print("   V4 Focusing Assets Generated!")
        await browser.close()

if __name__ == "__main__":
    asyncio.run(capture_final_v4())
