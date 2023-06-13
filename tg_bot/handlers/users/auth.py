from aiogram.types import Message

from tg_bot.config import DIS


@DIS.message_handler(commands=['start'])
async def send_welcome(msg: Message):
    await msg.answer('Hi')
