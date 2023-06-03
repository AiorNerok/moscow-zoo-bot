import dotenv
import asyncio
import logging
from aiogram import Bot, Dispatcher

from core.handlers import Home, Club_friend

logging.basicConfig(level=logging.INFO)

env = dict(dotenv.dotenv_values('./../.env.local'))


async def main():
    bot = Bot(env['TOKEN_BOT'])
    dp = Dispatcher()

    dp.include_routers(Home.router, Club_friend.router)

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__=="__main__":
    asyncio.run(main())