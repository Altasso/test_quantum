import asyncio
from aiogram import Bot, Dispatcher, F, Router
from aiogram.types import Message, CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.enums import ParseMode
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.client.default import DefaultBotProperties
import aiohttp
import os
from datetime import datetime

from dotenv import load_dotenv

load_dotenv()

API_URL = os.getenv("API_URL", "http://localhost:8000/api/blog")
BOT_TOKEN = os.getenv("BOT_TOKEN")

bot = Bot(
    token=BOT_TOKEN,
    default=DefaultBotProperties(parse_mode=ParseMode.HTML)
)
dp = Dispatcher(storage=MemoryStorage())
router = Router()



@dp.message(F.text == "/start")
async def start(message: Message):
    await message.answer("Команда /posts покажет список постов.")


@dp.message(F.text == "/posts")
async def posts(message: Message):
    async with aiohttp.ClientSession() as session:
        async with session.get(f"{API_URL}/posts") as resp:
            if resp.status != 200:
                await message.answer("Ошибка при получении постов.")
                return
            data = await resp.json()

    if not data:
        await message.answer("Постов пока нет.")
        return

    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text=post['title'], callback_data=f"post_{post['id']}")]
            for post in data
        ]
    )

    await message.answer("Выберите пост:", reply_markup=keyboard)


@dp.callback_query(F.data.startswith("post_"))
async def show_post(callback: CallbackQuery):
    await callback.answer()
    post_id = callback.data.split("_")[1]

    async with aiohttp.ClientSession() as session:
        async with session.get(f"{API_URL}/posts/{post_id}") as resp:
            if resp.status != 200:
                await callback.message.answer("Не удалось получить пост.")
                return
            post = await resp.json()

    created_at = datetime.fromisoformat(post["created_at"].replace("Z", "+00:00"))
    formatted_date = created_at.strftime("%d.%m.%Y %H:%M")
    text = f"<b>{post['title']}</b>\n\n{post['content']}\n\nДата: {formatted_date}"
    await callback.message.answer(text)


async def on_startup(dispatcher: Dispatcher):
    print("Bot started")


async def on_shutdown(dispatcher: Dispatcher):
    print("Bot stopped")


async def main():
    dp.include_router(router)
    dp.startup.register(on_startup)
    dp.shutdown.register(on_shutdown)

    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
