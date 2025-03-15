<<<<<<< HEAD
import os
import asyncio
import yt_dlp
from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor

# Танзимоти бот
TOKEN = "7857407693:AAE2ZUzoaOozYU54-NJMUGIh7SqTOAOt_Fc"  # Ба ҷои "YOUR_BOT_TOKEN" токени боти худро гузоред
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

# Функсияи зеркашии видео
async def download_instagram_video(url):
    output_path = "video.mp4"  # Номи файли ниҳоӣ

    ydl_opts = {
        'format': 'best',
        'outtmpl': output_path,
        'quiet': True
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        return output_path  # Агар бомуваффақият бошад, видеоро бармегардонад
    except Exception as e:
        print(f"Хатои зеркашӣ: {e}")
        return None

# Фармони /start
@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await message.answer("Ассалому алайкум! Истиноди видеои Instagram-ро фиристед, то онро зеркашӣ кунам.")

# Гирифтани истинод ва зеркашии видео
@dp.message_handler()
async def process_instagram_link(message: types.Message):
    url = message.text

    if "instagram.com" not in url:
        await message.answer("❌ Лутфан истиноди дурусти Instagram ворид кунед!")
        return

    await message.answer("🔄 Видео дар ҳоли зеркашӣ аст, лутфан интизор шавед...")

    video_path = await download_instagram_video(url)

    if video_path:
        with open(video_path, "rb") as video:
            await message.answer_video(video)
        os.remove(video_path)  # Пок кардани файл пас аз фиристодан
    else:
        await message.answer("❌ Хатогӣ! Видео зеркашӣ нашуд. Санҷед, ки истинод дуруст аст.")

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
=======
﻿import os
import asyncio
import yt_dlp
from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor

# Токенро дуруст таъриф кунед
TOKEN = "7857407693:AAE2ZUzoaOozYU54-NJMUGIh7SqTOAOt_Fc"  # Истифодаи токени воқеӣ
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

# Функсияи зеркашии видео
async def download_instagram_video(url):
    output_path = "video.mp4"
    ydl_opts = {
        'format': 'best',
        'outtmpl': output_path,
        'quiet': True
    }
    try:
        loop = asyncio.get_running_loop()
        await loop.run_in_executor(None, lambda: yt_dlp.YoutubeDL(ydl_opts).download([url]))
        return output_path
    except Exception as e:
        print(f"Хатои зеркашӣ: {e}")
        return None

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await message.answer("Ассалому алайкум! Истиноди видеои Instagram-ро фиристед.")

@dp.message_handler()
async def process_instagram_link(message: types.Message):
    url = message.text.strip()

    if "instagram.com" not in url:
        await message.answer("❌ Лутфан истиноди дурусти Instagram ворид кунед!")
        return

    await message.answer("🔄 Видео дар ҳоли зеркашӣ аст...")

    video_path = await download_instagram_video(url)

    if video_path and os.path.exists(video_path):
        with open(video_path, "rb") as video:
            await message.answer_video(video)
        os.remove(video_path)
    else:
        await message.answer("❌ Хатогӣ! Видео зеркашӣ нашуд.")

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
>>>>>>> f405d3d (Added Procfile and requirements)
