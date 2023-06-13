import os

from aiogram import Bot, Dispatcher

TELEGRAM_BOT_TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')

BOT = Bot(TELEGRAM_BOT_TOKEN)
DIS = Dispatcher(BOT)  # Dispatcher
