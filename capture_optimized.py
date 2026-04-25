import asyncio
import os
from playwright.async_api import async_playwright

OUT = os.path.dirname(os.path.abspath(__file__))

async def capture_optimized():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        # Scale factor 3.5 for absolute sharpness in full-width figures
        context = await browser.new_context(
            viewport={"width": 1280, "height": 900},
            device_scale_factor=3.5
        )
        page = await context.new_page()
        page.set_default_timeout(90000)

        print("2. Loading Optimized UI Capture (3.5x DPI)...")
        await page.goto("https://bidayuhjagoy.vercel.app/", wait_until="networkidle")
        
        # Input Bible-based Anchor Example
        await page.locator("textarea").first.fill("tell these stones to become bread")
        await page.locator("#translateBtn").click()
        print("   Waiting for translation synthesis...")
        await page.locator("#translateBtn:not(:has-text('Sending'))").wait_for(timeout=120000)
        await page.wait_for_timeout(4000) 

        # --- Capture Component A: Translation Card ---
        # Look for the formal-card that contains the result
        print("   Capturing Main Result Card...")
        # Target based on class and inner content to be precise
        await page.locator("div.formal-card:has(h2:has-text('Dashboard')), div.formal-card:has(h2:has-text('Bulk'))").first.screenshot(path=f"{OUT}/fig_main_ui_highres.png")
        
        # --- Capture Component B: Analysis Card ---
        print("   Capturing Analysis Card...")
        # Toggle Analysis if needed (assuming it's collapsible)
        await page.evaluate("window.scrollTo(0, document.body.scrollHeight)")
        await page.wait_for_timeout(1000)
        
        # Selector based on find_ids.py output
        analysis_locator = page.locator("#sentenceDetailPanel, div.formal-card:has(h3:has-text('Analysis'))").first
        # Force it to be visible if hidden
        await page.evaluate('''(sel) => {
            const el = document.querySelector(sel);
            if (el) el.classList.remove('hidden');
        }''', "#sentenceDetailPanel")
        
        await analysis_locator.screenshot(path=f"{OUT}/fig_analysis_highres.png")

        print("   Optimized figures generated successfully!")
        await browser.close()

if __name__ == "__main__":
    asyncio.run(capture_optimized())
