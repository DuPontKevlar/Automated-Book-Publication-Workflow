from playwright.async_api import async_playwright
import asyncio

class WebScraper:
    def __init__(self, config):
        self.config = config

    async def scrape_content(self, url):
        async with async_playwright() as p:
            browser = await p.chromium.launch()
            page = await browser.new_page()
            await page.goto(url)
            content = await page.inner_text("main")
            screenshot_path = f"{self.config.output_dir}/screenshots/screenshot_{int(time.time())}.png"
            await page.screenshot(path=screenshot_path)
            await browser.close()
            return url.split("/")[-1], content.strip(), screenshot_path
