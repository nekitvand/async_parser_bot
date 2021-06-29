from dotenv import load_dotenv,find_dotenv
import os

load_dotenv(find_dotenv())

BOT_TOKEN = str(os.getenv("BOT_TOKEN"))
CHAT_ID = str(os.getenv("CHAT_ID"))