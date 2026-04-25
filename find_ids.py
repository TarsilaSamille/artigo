import asyncio
from playwright.async_api import async_playwright

async def find_ids():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()
        await page.goto("https://bidayuhjagoy.vercel.app/", wait_until="networkidle")
        
        await page.locator("textarea").first.fill("stones to bread")
        await page.locator("#translateBtn").click()
        await page.wait_for_timeout(5000)
        
        # Look for headers containing "Linguistic" or "Analysis" or "History"
        headers = await page.evaluate('''() => {
            return Array.from(document.querySelectorAll('h2, h3, h4, h5')).map(h => ({
                text: h.innerText,
                parentId: h.parentElement.id,
                parentClass: h.parentElement.className,
                grandParentId: h.parentElement.parentElement ? h.parentElement.parentElement.id : null
            }));
        }''')
        
        for h in headers:
            print(f"Header: {h['text']} | ParentID: {h['parentId']} | ParentClass: {h['parentClass']} | GrandParentID: {h['grandParentId']}")
            
        await browser.close()

if __name__ == "__main__":
    asyncio.run(find_ids())
