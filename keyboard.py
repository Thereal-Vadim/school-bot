from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

def simple_menu():
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(KeyboardButton("Привет"))
    keyboard.add(KeyboardButton("Пока"))
    return keyboard

def links_menu():
    keyboard = InlineKeyboardMarkup()
    keyboard.add(InlineKeyboardButton("Новости школы", url="https://example.com/news"))
    keyboard.add(InlineKeyboardButton("Расписание", url="https://example.com/schedule"))
    keyboard.add(InlineKeyboardButton("Видео с занятиями", url="https://example.com/videos"))
    return keyboard

def dynamic_menu():
    keyboard = InlineKeyboardMarkup()
    keyboard.add(InlineKeyboardButton("Показать больше", callback_data="show_more"))
    return keyboard

def expanded_menu():
    keyboard = InlineKeyboardMarkup()
    keyboard.add(InlineKeyboardButton("Опция 1", callback_data="option_1"))
    keyboard.add(InlineKeyboardButton("Опция 2", callback_data="option_2"))
    return keyboard
