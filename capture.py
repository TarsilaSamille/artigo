"""
Playwright script - Round 2: longer wait for translation, capture Grammar/Dict tabs, History detail
"""
import asyncio
import os
from playwright.async_api import async_playwright

OUT = os.path.dirname(os.path.abspath(__file__))

async def capture():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page(viewport={"width": 1440, "height": 900})
        page.set_default_timeout(60000)

        print("1. Loading main page...")
        await page.goto("https://bidayuhjagoy.vercel.app/", wait_until="networkidle")
        
        # Type the sentence and translate
        await page.locator("textarea").first.fill("The very dark river flowed past our village.")
        await page.locator("#translateBtn").click()
        print("   Waiting for translation to complete (up to 90s)...")
        # Wait for the button to go back to "Translate" text (i.e. no longer "Sending...")
        await page.locator("#translateBtn:not(:has-text('Sending'))").wait_for(timeout=90000)
        await page.wait_for_timeout(2000)  # small buffer for DOM updates
        await page.screenshot(path=f"{OUT}/fig_main_ui.png", full_page=False)
        print("   Saved fig_main_ui.png (translation result)")

        # Scroll down to capture full results
        await page.evaluate("window.scrollTo(0, 500)")
        await page.wait_for_timeout(500)
        await page.screenshot(path=f"{OUT}/fig_translation_result.png", full_page=False)
        print("   Saved fig_translation_result.png")

        # Full page screenshot
        await page.screenshot(path=f"{OUT}/fig_full_page.png", full_page=True)
        print("   Saved fig_full_page.png")
        
        # --- Grammar tab ---
        print("2. Clicking Grammar tab...")
        try:
            await page.locator("button.tab-button[onclick*='grammar']").click()
            await page.wait_for_timeout(2000)
            await page.screenshot(path=f"{OUT}/fig_grammar.png", full_page=True)
            print("   Saved fig_grammar.png")
        except Exception as e:
            print(f"   Failed to capture Grammar: {e}")

        # --- Dictionary tab ---
        print("3. Clicking Dictionary tab...")
        try:
            await page.locator("button.tab-button[onclick*='dictionary']").click()
            await page.wait_for_timeout(2000)
            await page.screenshot(path=f"{OUT}/fig_dictionary.png", full_page=False)
            print("   Saved fig_dictionary.png")
        except Exception as e:
            print(f"   Failed to capture Dictionary: {e}")

        # --- Corpus tab ---
        print("4. Clicking Corpus tab...")
        try:
            await page.locator("button.tab-button[onclick*='corpus']").click()
            await page.wait_for_timeout(2000)
            await page.screenshot(path=f"{OUT}/fig_corpus.png", full_page=False)
            print("   Saved fig_corpus.png")
        except Exception as e:
            print(f"   Failed to capture Corpus: {e}")

        # --- History tab ---
        print("5. Clicking History tab...")
        try:
            await page.locator("button.tab-button[onclick*='history']").click()
            await page.wait_for_timeout(2000)
            # Scroll to first item
            await page.screenshot(path=f"{OUT}/fig_history_top.png", full_page=False)
            print("   Saved fig_history_top.png")
        except Exception as e:
            print(f"   Failed to capture History: {e}")

        # --- Translator tab again to capture analysis section properly ---
        print("6. Going back to Translator for analysis...")
        try:
            await page.locator("button.tab-button[onclick=\"switchTab('translator')\"]").click()
            await page.wait_for_timeout(1000)
        except Exception as e:
            print(f"   Failed to switch back to Translator: {e}")

        # Re-do the translation
        await page.locator("textarea").first.fill("The river provides water for the village.")
        await page.locator("#translateBtn").click()
        print("   Waiting for translation to complete (up to 90s)...")
        await page.locator("#translateBtn:not(:has-text('Sending'))").wait_for(timeout=90000)
        await page.wait_for_timeout(2000)
        # Scroll all the way down to capture analysis
        await page.evaluate("window.scrollTo(0, document.body.scrollHeight)")
        await page.wait_for_timeout(1000)
        await page.screenshot(path=f"{OUT}/fig_analysis.png", full_page=False)
        print("   Saved fig_analysis.png")
        
        # Scroll up to capture result box
        await page.evaluate("window.scrollTo(0, 300)")
        await page.screenshot(path=f"{OUT}/fig_result_box.png", full_page=False)
        print("   Saved fig_result_box.png")

        await browser.close()
        print("\nAll done!")

asyncio.run(capture())
