from aiogram.utils import executor
from django.core.management.base import BaseCommand

from tg_bot.config import DIS
from tg_bot.handlers import init


class Command(BaseCommand):
    help = "Start TelegramBot as polling"

    def handle(self, *args, **options):
        if __name__ == 'tg_bot.management.commands.start_polling':
            init()
        executor.start_polling(DIS, skip_updates=True)
