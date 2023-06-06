import logging
import asyncio
from aiogram import Bot, Dispatcher, types

from config import config
from core.handlers import map,QRCode

logging.basicConfig(level=logging.INFO)

bot = Bot(config["TOKEN_BOT"])
dp = Dispatcher()

async def main():

    bot_commands = [
        types.BotCommand(command="/help", description="Get info about me"),
        types.BotCommand(command="/map", description="Show map zoo"),
        types.BotCommand(command="/chat", description="set bot for free chat")
    ]

    dp.include_routers(map.router, QRCode.router)

    try:
        await bot.set_my_commands(bot_commands)
        await dp.start_polling(bot)
    finally:
        await bot.session.close()


if __name__ == '__main__':
    asyncio.run(main())