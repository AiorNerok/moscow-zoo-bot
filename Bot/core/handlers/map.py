from aiogram import Router
from aiogram.types import Message, BufferedInputFile
from aiogram.filters import Command 

router = Router()

@router.message(Command('map'))
async def show_map(message: Message):
    with open('core/assets/map.jpg', 'rb') as photo_map:
        await message.answer_photo(
            BufferedInputFile(photo_map.read(), filename='map.jpg'),
            caption="Карта Московского Зоопарка"
        )