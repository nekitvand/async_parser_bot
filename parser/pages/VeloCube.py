from playwright.async_api import Page


class VeloCubeLocators:
    status = ".product_stock-status"
    CHOOSE_SIZE = ".variant_name"


class VeloCubePage:
    URL = "https://velocube.ru/products/merida-silex-400-2021"

    def __init__(self, page: Page):
        self.page = page

    async def open_page(self, url):
        await self.page.goto(url)

    async def get_all_elements(self):
        elements = await self.page.query_selector_all(VeloCubeLocators.CHOOSE_SIZE)
        return elements

    async def get_status_text(self) -> str:
        result = await self.page.inner_text(selector=VeloCubeLocators.status, timeout=50000)
        return result

    async def check_status(self) -> bool:
        status = await self.get_status_text()
        if status != "Ожидается" or "Нет в наличии":
            return False
        return True

    async def check_status_for_all_element(self):
        status = {}
        elements = await self.get_all_elements()
        for element in elements:
            size = await element.text_content()
            if "XS" and "LIME" in size:
                await element.click()
                result = await self.check_status()
                status.update({"lime": result})
            elif "XS" and "BLUE" in size:
                await element.click()
                result = await self.check_status()
                status.update({"blue": result})
        return [status]
