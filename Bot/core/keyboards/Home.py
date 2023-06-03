from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.keyboard import ReplyKeyboardBuilder

def home_kb() -> ReplyKeyboardMarkup:
    builder = ReplyKeyboardBuilder()

    builder.row(KeyboardButton(text="Клуб Друзей"))
    builder.row(KeyboardButton(text="Викторины"),KeyboardButton(text="Гид"))
    builder.row(KeyboardButton(text="Настройки"))
    builder.row(KeyboardButton(text="ЧАВО"))
    
    return  builder.as_markup(resize_keyboard=True)