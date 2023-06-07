import logging
import asyncio
from aiogram import Bot, Dispatcher, types

from config import config
from core.handlers import MenuButtons

logging.basicConfig(level=logging.INFO)

bot = Bot(config["TOKEN_BOT"])
dp = Dispatcher()

async def main():

    bot_commands = [
        types.BotCommand(command="/help", description="Описание быстрых команд"),
        types.BotCommand(command="/map",  description="Получить карту Московского Зоопарка"),
        types.BotCommand(command="/events",  description="Последние события"),
        types.BotCommand(command="/feedback",  description="Оставить отзыв"),
    ]

    dp.include_routers(MenuButtons.router)

    try:
        await bot.set_my_commands(bot_commands)
        await dp.start_polling(bot)
    finally:
        await bot.session.close()


if __name__ == '__main__':
    asyncio.run(main())