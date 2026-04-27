import asyncio
import os
from playwright.async_api import async_playwright

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DIAGRAMS = f"{ROOT}/diagrams"
FIGURES = f"{ROOT}/figures"

async def render_mermaid_ultrares(filename):
    with open(f"{DIAGRAMS}/{filename}.mmd", "r") as f:
        mmd_content = f.read()

    html_content = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <script src="https://cdn.jsdelivr.net/npm/mermaid@10/dist/mermaid.min.js"></script>
        <style>
            body {{  margin: 0; padding: 20px; }}
            #graph {{ display: inline-block; }}
            .mermaid svg {{ font-family: 'Times New Roman', serif !important; }}
        </style>
    </head>
    <body>
        <div id="graph" class="mermaid">
        {mmd_content}
        </div>
        <script>
            mermaid.initialize({{ 
                startOnLoad: true, 
                fontSize: 32,
                fontFamily: 'serif'
            }});
        </script>
    </body>
    </html>
    """
    
    html_path = f"{ROOT}/scripts/ultra_render.html"
    with open(html_path, "w") as f:
        f.write(html_content)

    async with async_playwright() as p:
        browser = await p.chromium.launch()
        # Scale factor 3.0 for 4K-like sharpness in diagrams
        context = await browser.new_context(device_scale_factor=3.0)
        page = await context.new_page()
        await page.goto(f"file://{html_path}")
        
        await page.wait_for_selector(".mermaid svg")
        element = await page.query_selector(".mermaid svg")
        box = await element.bounding_box()
        
        await page.screenshot(
            path=f"{FIGURES}/fig_{filename}_highres.png", 
            clip=box,
            omit_background=True
        )
        print(f"   Ultra-res fig_{filename}_highres.png generated in figures/.")
        await browser.close()
    
    os.remove(html_path)

async def main():
    print("1. Rendering Ultra-High-Res Diagrams...")
    await render_mermaid_ultrares("arch")
    await render_mermaid_ultrares("pipeline")
    print("   Diagrams Done!")

if __name__ == "__main__":
    asyncio.run(main())
