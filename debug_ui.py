import asyncio
from playwright.async_api import async_playwright

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()
        
        # Capture console messages
        page.on("console", lambda msg: print(f"Browser Console: {msg.text}"))
        
        # Capture unhandled exceptions
        page.on("pageerror", lambda err: print(f"Browser Error: {err.message}"))
        
        print("Opening localhost:8080...")
        try:
            await page.goto("http://localhost:8080", wait_until="networkidle", timeout=10000)
            print("Page loaded.")
            await page.wait_for_timeout(2000) # Wait a bit for JS to execute
        except Exception as e:
            print(f"Failed to load page: {e}")
            
        await browser.close()

if __name__ == "__main__":
    asyncio.run(main())
