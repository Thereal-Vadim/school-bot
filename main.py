import os
import asyncio
import sqlite3
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import CommandStart
from aiogram.types import Message

# Укажите ваш токен бота
BOT_TOKEN = "8129764148:AAFUnRwaJC3lUVgIPxmgBaniYXpH_z_QcZk"

# Создаем базу данных и таблицу
DB_PATH = "school_data.db"
conn = sqlite3.connect(DB_PATH)
cursor = conn.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    age INTEGER,
    grade TEXT)''')
conn.commit()
conn.close()

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

# Словарь для хранения временных данных пользователей
user_data = {}

@dp.message(CommandStart())
async def start_command(message: Message):
    await message.answer("Привет! Выбери опцию из меню:", reply_markup=get_main_keyboard())

@dp.message(F.text == "Привет")
async def say_hello(message: Message):
    await message.answer(f"Привет, {message.from_user.first_name}!")

@dp.message(F.text == "Пока")
async def say_goodbye(message: Message):
    await message.answer(f"До свидания, {message.from_user.first_name}!")

@dp.message(F.text == "/links")
async def send_links(message: Message):
    await message.answer("Выберите ссылку:", reply_markup=get_links_keyboard())

@dp.message(F.text == "/dynamic")
async def show_dynamic_menu(message: Message):
    await message.answer("Вот дополнительное меню:", reply_markup=get_dynamic_keyboard())

@dp.callback_query(F.data == "show_more")
async def show_more_options(callback: CallbackQuery):
    await callback.message.edit_reply_markup(reply_markup=get_expanded_keyboard())

@dp.callback_query(F.data == "option_1")
async def option_1_selected(callback: CallbackQuery):
    await callback.message.answer("Вы выбрали Опцию 1")

@dp.callback_query(F.data == "option_2")
async def option_2_selected(callback: CallbackQuery):
    await callback.message.answer("Вы выбрали Опцию 2")

async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())