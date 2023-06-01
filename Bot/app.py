import dotenv

from aiogram import Bot, Dispatcher, executor, types

from aiogram.types import InlineKeyboardButton,ReplyKeyboardMarkup, KeyboardButton

from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, KeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove

env = dict(dotenv.dotenv_values('./../.env.local'))


bot = Bot(env['TOKEN_BOT'])

dp = Dispatcher(bot=bot)


@dp.message_handler(commands=["start"])
async def start_command(msg: types.Message):
    id = msg.from_user.id
    bot.delete_message
    await bot.send_message(id, 'msg')

executor.start_polling(dp)