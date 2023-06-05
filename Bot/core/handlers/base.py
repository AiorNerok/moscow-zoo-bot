import requests
from aiogram import types, Bot, enums
from aiogram.utils import chat_action
from config import config
import io
from PIL import Image
from pyzbar.pyzbar import decode
import asyncio

async def parse_photo_on_qr_code(message: types.Message):

    if message.photo:
        photo = message.photo
        id_ = photo[-1].file_id
        get_path_ = requests.get(config["URI_PHOTO"]+id_)
        path_file = get_path_.json()['result']["file_path"]
        get_photo = requests.get(config["URI_PHOTO_PATH"]+path_file)
        img = Image.open(io.BytesIO(get_photo.content))
        qr_code = decode(img)

        if qr_code:
            result = str(qr_code[0].data)[2:-1]
            await message.answer(text=result)
        else:
            await message.answer(text="QR code not found =(")