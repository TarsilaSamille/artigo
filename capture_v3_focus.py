import asyncio
import os
from playwright.async_api import async_playwright

OUT = os.path.dirname(os.path.abspath(__file__))

async def capture_v3_focus():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        # Scale factor 2.0 with 300% CSS zoom produces huge, clean UI
        context = await browser.new_context(
            viewport={"width": 1600, "height": 1800},
            device_scale_factor=2.0
        )
        page = await context.new_page()
        page.set_default_timeout(120000)

        print("1. Loading Dashboard at 300% Zoom...")
        await page.goto("https://bidayuhjagoy.vercel.app/", wait_until="networkidle")
        
        # Apply 300% CSS Zoom
        await page.evaluate("document.body.style.zoom = '3.0'")
        await page.wait_for_timeout(2000)

        # Input the Strong Example
        await page.locator("textarea").first.fill("tell these stones to become bread")
        await page.locator("#translateBtn").click()
        print("   Synthesizing translation analysis...")
        await page.wait_for_selector("text=batuh-batuh", timeout=120000)
        await page.wait_for_timeout(3000)

        # --- Capture A: Main Translator View (Zoomed) ---
        print("   Capturing Main UI (300% Zoom)...")
        # Scroll to top
        await page.evaluate("window.scrollTo(0, 0)")
        # Clip the top dashboard section
        await page.screenshot(path=f"{OUT}/fig_main_ui_zoom300.png", clip={"x": 50, "y": 150, "width": 1500, "height": 1200})

        # --- Capture B: Translation Analysis (Zoomed) ---
        print("   Capturing Analysis Section (300% Zoom)...")
        # Scroll to analysis
        await page.evaluate("window.scrollTo(0, 1600)")
        await page.wait_for_timeout(1000)
        # Identify the analysis card
        analysis_locator = page.locator("#sentenceDetailPanel").first
        await page.evaluate('''(sel) => {
            const el = document.querySelector(sel);
            if (el) el.classList.remove('hidden');
        }''', "#sentenceDetailPanel")
        await analysis_locator.screenshot(path=f"{OUT}/fig_analysis_zoom300.png")

        # --- Capture C: Full Prompt (Debug) ---
        print("   Expanding 'Full Prompt (Debug)'...")
        # Find the summary based on my previous find_debug.py research
        debug_summary = page.locator("summary:has-text('View Full Prompt')").first
        await debug_summary.click()
        await page.wait_for_timeout(2000)
        
        print("   Capturing Debug Trace...")
        # Target the now-visible debug container or just the area
        debug_card = page.locator("#sentenceDetailPanel pre").first # Assuming pre for JSON
        if await debug_card.count() > 0:
            await debug_card.screenshot(path=f"{OUT}/fig_debug_zoom300.png")
        else:
            # Fallback to clip if locator fails
            await page.screenshot(path=f"{OUT}/fig_debug_zoom300.png", clip={"x": 50, "y": 2800, "width": 1500, "height": 1000})

        print("   All 300% zoomed assets generated!")
        await browser.close()

if __name__ == "__main__":
    asyncio.run(capture_v3_focus())
