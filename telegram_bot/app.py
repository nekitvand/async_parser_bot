from aiogram import Bot, Dispatcher
from telegram_bot.config import BOT_TOKEN, CHAT_ID


class BotApp:

    def __init__(self):
        self.bot = Bot(BOT_TOKEN)
        self.dp = Dispatcher(self.bot)
        self.chat_id = CHAT_ID

    async def send_message_to_channel(self, text):
        if text is None or len(text) == 0:
            return False
        try:
            await self.bot.send_message(chat_id=self.chat_id, text=text)
        finally:
            await self.bot.session.close()
