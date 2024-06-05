import logging
from aiogram import Bot, Dispatcher, types
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.filters import Command
from aiogram.utils.keyboard import InlineKeyboardBuilder
from tokens import BOT_TOKEN, WEB_APP_URL
import asyncio

# Настройка логирования
logging.basicConfig(level=logging.INFO)

# Инициализация бота и диспетчера
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

# Обработчик команды /start
@dp.message(Command(commands=['start']))
async def send_welcome(message: types.Message):
    keyboard = InlineKeyboardBuilder()
    user = message.from_user
    web_app_url_with_params = f"{WEB_APP_URL}?user_id={user.id}&first_name={user.first_name}&last_name={user.last_name}&username={user.username}"
    web_app_button = InlineKeyboardButton(text="Запустить Crypto Checker📈", web_app=types.WebAppInfo(url=web_app_url_with_params))
    keyboard.add(web_app_button)
    await message.answer("Привет! В Crypto Checker можно посмотреть курс валют 💲 и стоимость своего портфеля 💼.", reply_markup=keyboard.as_markup())

async def main():
    # Пропускать накопленные обновления и запускать бота
    await dp.start_polling(bot, skip_updates=True)

if __name__ == '__main__':
    asyncio.run(main())