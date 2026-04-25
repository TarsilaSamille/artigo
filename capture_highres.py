import asyncio
import os
from playwright.async_api import async_playwright

OUT = os.path.dirname(os.path.abspath(__file__))

async def capture_highres():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        # Scale factor 2.5 for extremely sharp UI
        context = await browser.new_context(
            viewport={"width": 1600, "height": 1000},
            device_scale_factor=2.5
        )
        page = await context.new_page()
        page.set_default_timeout(60000)

        print("1. Loading High-DPI UI...")
        await page.goto("https://bidayuhjagoy.vercel.app/", wait_until="networkidle")
        
        # Type the "Strong Example" (Bible-based)
        await page.locator("textarea").first.fill("tell these stones to become bread")
        await page.locator("#translateBtn").click()
        print("   Waiting for translation (DPI 2.5)...")
        await page.locator("#translateBtn:not(:has-text('Sending'))").wait_for(timeout=90000)
        await page.wait_for_timeout(3000) 

        # --- Capture Main Translation Result Box ---
        print("2. Capturing Result Box...")
        # Target the specific result section
        result_box = await page.query_selector("#results-section") # Assuming this ID from UI
        if not result_box:
            # Fallback to a clip if ID is missing
            await page.screenshot(path=f"{OUT}/fig_main_ui_highres.png", clip={"x": 50, "y": 200, "width": 1500, "height": 600})
        else:
            await result_box.screenshot(path=f"{OUT}/fig_main_ui_highres.png")
        
        # --- Capture Analysis Section ---
        print("3. Capturing Analysis Section...")
        await page.evaluate("window.scrollTo(0, document.body.scrollHeight)")
        await page.wait_for_timeout(1000)
        # Target the full prompt / debug section
        analysis = await page.query_selector("#analysis-section")
        if not analysis:
             await page.screenshot(path=f"{OUT}/fig_analysis_highres.png", clip={"x": 50, "y": 800, "width": 1500, "height": 800})
        else:
            await analysis.screenshot(path=f"{OUT}/fig_analysis_highres.png")

        print("   UI Figures Generated!")
        await browser.close()

if __name__ == "__main__":
    asyncio.run(capture_highres())
