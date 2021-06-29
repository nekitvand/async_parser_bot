import asyncio
from parser.browser import Browser
from parser.business_scenarios_layer import Yandex, VeloGrad, VeloCube
from telegram_bot.app import BotApp
from playwright.async_api import async_playwright
from parser.transformation_layer import Checker


async def yandex_market(browser):
    yandex_script = Yandex(browser)
    yandex_market_task = [yandex_script.get_bike()]
    result = await asyncio.gather(*yandex_market_task)
    return {"YandexMarket": result}


async def velo_grad(browser):
    velo_grad_script = VeloGrad(browser)
    velo_grad = [
        velo_grad_script.check_black_bike(),
        velo_grad_script.check_blue_bike(),
        velo_grad_script.check_yellow_bike()
    ]
    result = await asyncio.gather(*velo_grad)
    return {"VeloGrad": result}

async def velo_cube(browser):
    velo_cube_script = VeloCube(browser)
    result = await asyncio.create_task(velo_cube_script.check_bike_xs_all_color())
    return {"VeloCube": result}


async def main():
    result = {}
    async with async_playwright() as playwright:
        browser = await Browser().init_browser(playwright)
        result.update(await velo_grad(browser))
        result.update(await velo_cube(browser))
        # result.update(await yandex_market(browser))
        ready = Checker().create_ready_list_with_strings(result)
        await BotApp().send_message_to_channel(Checker().combine_strings(ready))


if __name__ == '__main__':
    asyncio.run(main())
