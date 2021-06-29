from parser.pages.YandexMarket import YandexMarketPage
from parser.pages.VeloGrad import VeloGradPage
from parser.pages.VeloCube import VeloCubePage


class Yandex:

    def __init__(self, browser):
        self.browser = browser

    async def get_bike(self):
        context = await self.browser.new_context()
        page = await context.new_page()
        ya_page = YandexMarketPage(page)
        await ya_page.open_market()

        titles = await ya_page.finds_title_product()
        result = await ya_page.count_check(titles)
        return {"Любой": result}


class VeloGrad:

    def __init__(self, browser):
        self.browser = browser

    async def check_blue_bike(self):
        context = await self.browser.new_context()
        page = await context.new_page()
        velo_grad_page = VeloGradPage(page)
        await velo_grad_page.open_market(velo_grad_page.blue)
        result = await velo_grad_page.check_status()
        return {"blue": result}

    async def check_black_bike(self):
        context = await self.browser.new_context()
        page = await context.new_page()
        velo_grad_page = VeloGradPage(page)
        await velo_grad_page.open_market(velo_grad_page.black)
        result = await velo_grad_page.check_status()
        return {"black": result}

    async def check_yellow_bike(self):
        context = await self.browser.new_context()
        page = await context.new_page()
        velo_grad_page = VeloGradPage(page)
        await velo_grad_page.open_market(velo_grad_page.yellow)
        result = await velo_grad_page.check_status()
        return {"yellow": result}


class VeloCube:

    def __init__(self, browser):
        self.browser = browser

    async def check_bike_xs_all_color(self):
        context = await self.browser.new_context()
        page = await context.new_page()
        velo_cube = VeloCubePage(page)
        await velo_cube.open_page(velo_cube.URL)
        result = await velo_cube.check_status_for_all_element()
        return result
