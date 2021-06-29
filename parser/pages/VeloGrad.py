from playwright.async_api import Page


class VeloGradLocators:
    status = ".store_view.dotted"


class VeloGradPage:
    blue = "https://www.velograd.ru/catalog/graviynye-velosipedy/velosiped-merida-silex-400-28-2021/?oid=53136"
    black = "https://www.velograd.ru/catalog/graviynye-velosipedy/velosiped-merida-silex-400-28-2021/?oid=53126"
    yellow = "https://www.velograd.ru/catalog/graviynye-velosipedy/velosiped-merida-silex-400-28-2021/?oid=53131"

    def __init__(self, page: Page):
        self.page = page

    async def open_market(self, url: str):
        await self.page.goto(url)

    async def get_status_text(self) -> str:
        result = await self.page.inner_text(selector=VeloGradLocators.status, timeout=50000)
        return result

    async def check_status(self) -> bool:
        status = await self.get_status_text()
        if status == "В наличии":
            return True
        return False
