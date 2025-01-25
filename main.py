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
    user_data[message.from_user.id] = {}
    await message.answer("Привет! Как тебя зовут?")


@dp.message(F.text)
async def handle_input(message: Message):
    user_id = message.from_user.id
    text = message.text.strip()

    if user_id not in user_data or 'name' not in user_data[user_id]:
        if not text.isalpha():
            await message.answer("Имя должно содержать только буквы. Попробуй еще раз.")
            return
        user_data[user_id] = {'name': text}
        await message.answer("Сколько тебе лет?")

    elif 'age' not in user_data[user_id]:
        if not text.isdigit():
            await message.answer("Пожалуйста, введи возраст числом.")
            return
        user_data[user_id]['age'] = int(text)
        await message.answer("В каком ты классе?")

    elif 'grade' not in user_data[user_id]:
        user_data[user_id]['grade'] = text
        await save_to_db(user_id)
        await message.answer("Спасибо! Твои данные сохранены.")
        del user_data[user_id]


async def save_to_db(user_id):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    data = user_data.get(user_id)
    if data:
        cursor.execute("INSERT INTO students (name, age, grade) VALUES (?, ?, ?)",
                       (data['name'], data['age'], data['grade']))
        conn.commit()
    conn.close()



async def main():
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
