from aiogram.types import Message
from aiogram.filters.text import Text
from aiogram import  Router
from aiogram.filters import CommandStart

from core.keyboards.Home import home_kb

router = Router()

@router.message(CommandStart())
async def Home(message:Message):
    await message.answer('Добро пожаловать', reply_markup=home_kb())
