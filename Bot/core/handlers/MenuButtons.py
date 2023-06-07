from aiogram import Router, F, Router
from aiogram.types import Message, BufferedInputFile
from aiogram.filters import Command 

from PIL import Image
from pyzbar import pyzbar

from app import bot

router = Router()

@router.message(F.photo)
async def QRCode(message: Message):
    await bot.download(
        message.photo[-1],
        destination=f"core/assets/{message.photo[-1].file_id}.jpg"
    )

    result = pyzbar.decode(Image.open(f"core/assets/{message.photo[-1].file_id}.jpg"))
    print(result)

    await message.answer(text="photo")


@router.message(Command('help'))
async def answer_help_request(message: Message):
    await message.answer("""
    simple description commands
    
    */map* \- send map mosckow zoo
    */*
    """, parse_mode="MarkdownV2")

@router.message(Command('map'))
async def show_map(message: Message):
    with open('core/assets/map.jpg', 'rb') as photo_map:
        await message.answer_photo(
            BufferedInputFile(photo_map.read(), filename='map.jpg'),
            caption="Карта Московского Зоопарка"
        )