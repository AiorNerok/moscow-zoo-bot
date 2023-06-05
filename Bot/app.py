import asyncio
import logging
from aiogram import Bot, Dispatcher, types, F
from core.handlers import base
from config import config

logging.basicConfig(level=logging.INFO)



async def main():
    bot = Bot(config['TOKEN_BOT'])
    dp = Dispatcher()

    bot_commands = [
        types.BotCommand(command="/start", description="Run bot"),
        types.BotCommand(command="/map", description="Show map zoo")
    ]

    await bot.set_my_commands(bot_commands)

    dp.message.register(base.parse_photo_on_qr_code)

    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()

if __name__=="__main__":
    asyncio.run(main())