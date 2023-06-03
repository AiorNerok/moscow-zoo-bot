from aiogram.types import Message
from aiogram.filters.text import Text
from aiogram import  Router

from core.keyboards.Home import home_kb,club_friends_kb

router = Router()

@router.message(Text(text="Клуб Друзей", ignore_case=True))
async def club_friends(message: Message):
    await message.answer_photo(
        photo="https://www.justbenice.ru/wp-content/uploads/2017/08/justbenice-moscowzoo-20.jpg",
        caption="*Клуб друзей Московского Зоопарка*\ \n\nВ рамках Программы лояльности Московского зоопарка любой желающий может взять одно из животных под свою опеку\. Все — от маленьких посетителей до больших корпораций, — кто неравнодушен к жизни обитателей зоопарка, может стать участником программы\.",
        parse_mode="MarkdownV2",
        reply_markup=club_friends_kb()
    )