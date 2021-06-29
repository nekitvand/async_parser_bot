from playwright.async_api import Page


class YandexMarketLocators:
    TITLE_PRODUCT = "h3[data-zone-name='title'] a span"


class YandexMarketPage:

    MARKET_URL = "https://market.yandex.ru/product--shosseinyi-velosiped-merida-silex-400-2021/676664005/offers?track=tabs&onstock=1&grhow=supplier&local-offers-first=0"

    def __init__(self, page: Page):
        self.page = page

    async def open_market(self):
        await self.page.goto(self.MARKET_URL)

    async def finds_title_product(self):
        selectors = await self.page.query_selector_all(YandexMarketLocators.TITLE_PRODUCT)
        return selectors

    async def count_check(self, title):
        if len(title) > 0:
            return len(title)
        else:
            return False