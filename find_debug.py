import asyncio
from playwright.async_api import async_playwright

async def find_debug():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()
        await page.goto("https://bidayuhjagoy.vercel.app/", wait_until="networkidle")
        
        await page.locator("textarea").first.fill("tell these stones to become bread")
        await page.locator("#translateBtn").click()
        await page.wait_for_timeout(5000)
        
        # Look for the debug toggle
        elements = await page.evaluate('''() => {
            return [...document.querySelectorAll('button, summary, span, div')].filter(e => {
                const txt = e.innerText.toLowerCase();
                return txt.includes('debug') || txt.includes('full prompt') || txt.includes('analysis');
            }).map(e => ({
                text: e.innerText,
                tag: e.tagName,
                id: e.id,
                class: e.className
            }));
        }''')
        
        for el in elements:
            print(f"[{el['tag']}] {el['text']} | ID: {el['id']} | Class: {el['class']}")
            
        await browser.close()

if __name__ == "__main__":
    asyncio.run(find_debug())
