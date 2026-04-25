import asyncio
import os
from playwright.async_api import async_playwright

OUT = os.path.dirname(os.path.abspath(__file__))

async def capture_v3_v2():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        # Use a very tall viewport to avoid scroll issues
        context = await browser.new_context(
            viewport={"width": 1600, "height": 4000},
            device_scale_factor=2.0
        )
        page = await context.new_page()
        page.set_default_timeout(120000)

        print("1. Loading at 300% Zoom (Robust V2)...")
        await page.goto("https://bidayuhjagoy.vercel.app/", wait_until="networkidle")
        
        # Apply 300% CSS Zoom
        await page.evaluate("document.body.style.zoom = '3.0'")
        await page.wait_for_timeout(3000)

        # Input and Translate
        await page.locator("textarea").first.fill("tell these stones to become bread")
        await page.locator("#translateBtn").click()
        await page.wait_for_selector("text=batuh-batuh", timeout=120000)
        await page.wait_for_timeout(5000)

        # --- Capture A: Main UI ---
        print("   Capturing Main UI (300% Zoom)...")
        # Since zoom 3.0 effectively makes everything 3x larger, 
        # coordinates and dimensions in 'clip' need to account for this or 
        # use evaluate to get the actual rect.
        
        await page.screenshot(path=f"{OUT}/fig_main_ui_zoom300.png", clip={"x": 0, "y": 0, "width": 1500, "height": 1800})

        # --- Capture B: Full Prompt ---
        print("   Expanding Full Prompt...")
        await page.evaluate("window.scrollTo(0, 1500)")
        # Click the summary
        await page.evaluate('''() => {
            const summary = [...document.querySelectorAll('summary')].find(s => s.innerText.includes('Full Prompt'));
            if (summary) summary.click();
            
            // Also ensure the analysis panel is visible
            const panel = document.querySelector('#sentenceDetailPanel');
            if (panel) panel.classList.remove('hidden');
        }''')
        await page.wait_for_timeout(3000)
        
        print("   Capturing Debug section...")
        # Take a large screenshot of the bottom half
        await page.screenshot(path=f"{OUT}/fig_debug_zoom300.png", clip={"x": 0, "y": 1800, "width": 1500, "height": 2200})

        print("   Optimized 300% zoomed assets (V2) generated!")
        await browser.close()

if __name__ == "__main__":
    asyncio.run(capture_v3_v2())
