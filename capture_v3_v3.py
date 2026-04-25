import asyncio
import os
from playwright.async_api import async_playwright

OUT = os.path.dirname(os.path.abspath(__file__))

async def capture_v3_v3():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        context = await browser.new_context(
            viewport={"width": 1600, "height": 4500},
            device_scale_factor=2.0
        )
        page = await context.new_page()
        page.set_default_timeout(120000)

        print("1. Loading Dashboard at 300% Zoom (V3 Final)...")
        await page.goto("https://bidayuhjagoy.vercel.app/", wait_until="networkidle")
        await page.evaluate("document.body.style.zoom = '3.0'")
        await page.wait_for_timeout(3000)

        await page.locator("textarea").first.fill("tell these stones to become bread")
        await page.locator("#translateBtn").click()
        await page.wait_for_selector("text=batuh-batuh", timeout=120000)
        await page.wait_for_timeout(5000)

        # --- Shot 1: Main Translator Card ---
        print("   Capturing fig_main_ui_zoom300.png...")
        await page.screenshot(path=f"{OUT}/fig_main_ui_zoom300.png", clip={"x": 0, "y": 0, "width": 1500, "height": 1800})

        # Expand Debug
        await page.evaluate('''() => {
            const summary = [...document.querySelectorAll('summary')].find(s => s.innerText.includes('Full Prompt'));
            if (summary) summary.click();
            const panel = document.querySelector('#sentenceDetailPanel');
            if (panel) panel.classList.remove('hidden');
        }''')
        await page.wait_for_timeout(3000)

        # --- Shot 2: Linguistic Analysis (Reasoning Chain) ---
        print("   Capturing fig_analysis_zoom300.png...")
        # The Reasoning starts around y=1800 in the 300% zoomed world
        await page.screenshot(path=f"{OUT}/fig_analysis_zoom300.png", clip={"x": 0, "y": 1800, "width": 1500, "height": 1200})

        # --- Shot 3: Full Prompt (Debug JSON) ---
        print("   Capturing fig_debug_zoom300.png...")
        # The Debug JSON is lower down
        await page.screenshot(path=f"{OUT}/fig_debug_zoom300.png", clip={"x": 0, "y": 2800, "width": 1500, "height": 1500})

        print("   All 3 high-res 300% assets generated!")
        await browser.close()

if __name__ == "__main__":
    asyncio.run(capture_v3_v3())
