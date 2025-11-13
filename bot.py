import asyncio
import requests
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command

BOT_TOKEN = "8455252838:AAHQ3IO3w_dxqgpYbDrZmVcu6_JQ8IgGBo8"
API_URL = "https://api.fayzlixonadonlar.uz/utils/waitlist/"

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()


@dp.message(Command("start"))
async def start(message: types.Message):
    await message.answer("👋 Salom! Ma'lumotlarni ko‘rish uchun /list buyrug‘ini bosing.")


@dp.message(Command("list"))
async def show_waitlist(message: types.Message):
    try:
        response = requests.get(API_URL)
        data = response.json()

        if not data:
            await message.answer("📭 Bazada hozircha hech qanday so‘rov yo‘q.")
            return

        for item in data[:5]:
            text = (
                f"👤 Ism: {item['full_name']}\n"
                f"📧 Email: {item['email']}\n"
                f"📞 Telefon: {item['phone_number']}\n"
                f"📝 Mavzu: {item['theme']}\n"
                f"💬 Xabar: {item['message']}\n"
                f"📅 Sana: {item['date']}\n"
                "------------------------"
            )
            await message.answer(text)

    except Exception as e:
        await message.answer(f"❌ Xatolik: {e}")


async def main():
    print("🤖 Bot ishga tushdi...")
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
