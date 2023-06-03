from aiogram.types import Message
from aiogram.filters.text import Text
from aiogram import  Router
from aiogram.filters import CommandStart

router = Router()

@router.message(Text(text="гид", ignore_case=True))
async def guide(message: Message):
    await message.answer