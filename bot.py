import os
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
