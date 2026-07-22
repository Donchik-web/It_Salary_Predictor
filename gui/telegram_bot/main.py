import os

from dotenv import load_dotenv
from aiogram import Bot, Dispatcher
from gui.telegram_bot.handlers.handlers import router


load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

dp.include_router(router=router)

if __name__ == '__main__':
    dp.run_polling(bot)
