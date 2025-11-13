import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from datetime import datetime
import requests

BOT_TOKEN = "8455252838:AAHQ3IO3w_dxqgpYbDrZmVcu6_JQ8IgGBo8"
API_URL_ALL = "https://api.fayzlixonadonlar.uz/utils/waitlist/"
API_URL_DAILY = "https://api.fayzlixonadonlar.uz/utils/daily_waitlist/"

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()


@dp.message(Command("start"))
async def start(message: types.Message):
    await message.answer("👋 Salom! Kunlik so`rovlarni ko‘rish uchun /dailylist buyrug‘ini bosing. Barcha so`rovlarni ko`rish uchun esa /list buyrug`ini. ")


@dp.message(Command("list"))
async def show_waitlist(message: types.Message):
    await fetch_and_send_waitlist(message, API_URL_ALL)


@dp.message(Command("dailylist"))
async def show_daily_waitlist(message: types.Message):
    await fetch_and_send_waitlist(message, API_URL_DAILY)


async def fetch_and_send_waitlist(message: types.Message, url: str):
    try:
        response = requests.get(url)
        data = response.json()

        if not data:
            await message.answer("📭 Bazada hozircha hech qanday so‘rov yo‘q.")
            return

        for item in data[:5]:
            iso_date = item['date']
            try:
                dt = datetime.fromisoformat(iso_date)
                formatted_date = dt.strftime("%d-%m-%Y %H:%M")
            except:
                formatted_date = iso_date

            text = (
                f"👤 Ism: {item['full_name']}\n"
                f"📧 Email: {item['email']}\n"
                f"📞 Telefon: {item['phone_number']}\n"
                f"📝 Mavzu: {item['theme']}\n"
                f"💬 Xabar: {item['message']}\n"
                f"📅 Sana: {formatted_date}\n"
            )
            await message.answer(text)

    except Exception as e:
        await message.answer(f"❌ Xatolik: {e}")


async def main():
    print("🤖 Bot ishga tushdi...")
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
