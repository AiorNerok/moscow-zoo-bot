from aiogram import Router, F
from aiogram.types import Message
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
