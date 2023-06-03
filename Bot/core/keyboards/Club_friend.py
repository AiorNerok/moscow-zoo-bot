from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.keyboard import ReplyKeyboardBuilder

def club_friends_kb()->ReplyKeyboardBuilder:
    kb=[[InlineKeyboardButton(text="Узнать по подробнее", url="https://www.justbenice.ru/work/moscowzoo/")]]
    
    return InlineKeyboardMarkup(inline_keyboard=kb)
