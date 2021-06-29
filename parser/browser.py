class Browser:

    async def init_browser(self, playwright):
        chromium = playwright.chromium
        browser = await chromium.launch(headless=False)
        return browser
