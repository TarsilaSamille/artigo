import asyncio
import os
from playwright.async_api import async_playwright

OUT = os.path.dirname(os.path.abspath(__file__))

async def capture_optimized():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        # Using a very wide but high viewport for clarity
        context = await browser.new_context(
            viewport={"width": 1400, "height": 1600},
            device_scale_factor=3.5
        )
        page = await context.new_page()
        page.set_default_timeout(120000)

        print("2. Loading Optimized UI Capture (v2, 3.5x DPI)...")
        await page.goto("https://bidayuhjagoy.vercel.app/", wait_until="networkidle")
        
        # Type the Bible-based Example
        await page.locator("textarea").first.fill("tell these stones to become bread")
        await page.locator("#translateBtn").click()
        print("   Waiting for translation synthesis...")
        
        # Wait for the result to appear (text 'batuh-batuh')
        await page.wait_for_selector("text=batuh-batuh", timeout=120000)
        await page.wait_for_timeout(5000) 

        # --- Capture Component A: Translation Card ---
        print("   Capturing Main Result Card...")
        # We know about x:50, y:200 from previous attempts, let's refine
        # We attempt to find the result container
        await page.screenshot(path=f"{OUT}/fig_main_ui_highres.png", clip={"x": 50, "y": 150, "width": 1300, "height": 600})
        
        # --- Capture Component B: Analysis Card ---
        print("   Capturing Analysis Section...")
        # Scroll down
        await page.evaluate("window.scrollTo(0, 800)")
        await page.wait_for_timeout(2000)
        
        # Attempt to capture the analysis area (middle-bottom of the page)
        await page.screenshot(path=f"{OUT}/fig_analysis_highres.png", clip={"x": 50, "y": 750, "width": 1300, "height": 800})

        print("   Optimized figures v2 generated!")
        await browser.close()

if __name__ == "__main__":
    asyncio.run(capture_optimized())
