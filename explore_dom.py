import asyncio
import os
from playwright.async_api import async_playwright

async def explore_dom():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()
        await page.goto("https://bidayuhjagoy.vercel.app/", wait_until="networkidle")
        
        await page.locator("textarea").first.fill("tell these stones to become bread")
        await page.locator("#translateBtn").click()
        await page.locator("#translateBtn:not(:has-text('Sending'))").wait_for(timeout=90000)
        await page.wait_for_timeout(3000)
        
        # List all IDs and unique classes of divs
        elements = await page.evaluate('''() => {
            const divs = Array.from(document.querySelectorAll('div, section, article'));
            return divs.map(d => ({
                tag: d.tagName,
                id: d.id,
                className: d.className,
                textHead: d.innerText.substring(0, 30)
            })).filter(d => d.id || d.className);
        }''')
        
        for el in elements:
            print(f"{el['tag']} | ID: {el['id']} | Class: {el['className']} | Text: {el['textHead']}")
            
        await page.screenshot(path="debug_full_ui.png", full_page=True)
        await browser.close()

if __name__ == "__main__":
    asyncio.run(explore_dom())
