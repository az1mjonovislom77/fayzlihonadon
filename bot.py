import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from datetime import datetime
import requests
import json
import os

BOT_TOKEN = "8455252838:AAHQ3IO3w_dxqgpYbDrZmVcu6_JQ8IgGBo8"
API_URL_ALL = "https://api.fayzlixonadonlar.uz/utils/waitlist/"
API_URL_DAILY = "https://api.fayzlixonadonlar.uz/utils/daily_waitlist/"
USERS_FILE = "allowed_users.json"

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()
last_sent_id = None


def load_users():
    if os.path.exists(USERS_FILE):
        with open(USERS_FILE, "r") as f:
            return json.load(f)
    return []


def save_users(users):
    with open(USERS_FILE, "w") as f:
        json.dump(users, f)


allowed_users = load_users()


async def realtime_checker():
    global last_sent_id

    while True:
        try:
            response = requests.get(API_URL_ALL)
            data = response.json()

            if data:
                latest = data[0]
                current_id = latest.get("id")

                if last_sent_id is None:
                    last_sent_id = current_id

                elif current_id != last_sent_id:
                    last_sent_id = current_id

                    iso_date = latest.get('date', '')
                    try:
                        dt = datetime.fromisoformat(iso_date)
                        formatted_date = dt.strftime("%d-%m-%Y %H:%M")
                    except:
                        formatted_date = iso_date

                    text = (
                        "🚨 YANGI SO‘ROV KELDI!\n\n"
                        f"👤 Ism: {latest.get('full_name', '')}\n"
                        f"📧 Email: {latest.get('email', '')}\n"
                        f"📞 Telefon: {latest.get('phone_number', '')}\n"
                        f"📝 Mavzu: {latest.get('theme', '')}\n"
                        f"💬 Xabar: {latest.get('message', '')}\n"
                        f"📅 Sana: {formatted_date}"
                    )

                    for username in allowed_users:
                        try:
                            user = await bot.get_chat(username)
                            await bot.send_message(user.id, text)
                        except:
                            pass

        except Exception as e:
            print("Realtime error:", e)

        await asyncio.sleep(60)  # ⏱ 1 minut


@dp.message(Command("start"))
async def start(message: types.Message):
    username = message.from_user.username
    if username not in allowed_users:
        await message.answer("❌ Sizga ruxsat berilmagan.")
        return

    await message.answer(
        '''👋 Salom! Kunlik so`rovlarni ko‘rish uchun /dailylist buyrug‘ini, 
Barcha so`rovlarni ko`rish uchun esa /list buyrug`ini yuboring...''')


@dp.message(Command("list"))
async def show_waitlist(message: types.Message):
    username = message.from_user.username
    if username not in allowed_users:
        await message.answer("❌ Sizga ruxsat berilmagan.")
        return

    await fetch_and_send_waitlist(message, API_URL_ALL)


@dp.message(Command("dailylist"))
async def show_daily_waitlist(message: types.Message):
    username = message.from_user.username
    if username not in allowed_users:
        await message.answer("❌ Sizga ruxsat berilmagan.")
        return

    await fetch_and_send_waitlist(message, API_URL_DAILY)


@dp.message(Command("adduser"))
async def add_user(message: types.Message):
    admin_username = message.from_user.username
    if not allowed_users or admin_username != allowed_users[0]:
        await message.answer("❌ Faqat admin yangi foydalanuvchi qo'sha oladi.")
        return

    args = message.text.split()
    if len(args) != 2:
        await message.answer("❌ Foydalanish: /add_user <username>")
        return

    new_user = args[1].lstrip("@")
    if new_user in allowed_users:
        await message.answer("⚠️ Foydalanuvchi allaqachon ruxsatli.")
        return

    allowed_users.append(new_user)
    save_users(allowed_users)
    await message.answer(f"✅ @{new_user} foydalanuvchiga ruxsat berildi.")


async def fetch_and_send_waitlist(message: types.Message, url: str):
    try:
        response = requests.get(url)
        data = response.json()

        if not data:
            await message.answer("📭 Bazada hozircha hech qanday so‘rov yo‘q.")
            return

        for item in data[:5]:
            iso_date = item.get('date', '')
            try:
                dt = datetime.fromisoformat(iso_date)
                formatted_date = dt.strftime("%d-%m-%Y %H:%M")
            except:
                formatted_date = iso_date

            text = (
                f"👤 Ism: {item.get('full_name', '')}\n"
                f"📧 Email: {item.get('email', '')}\n"
                f"📞 Telefon: {item.get('phone_number', '')}\n"
                f"📝 Mavzu: {item.get('theme', '')}\n"
                f"💬 Xabar: {item.get('message', '')}\n"
                f"📅 Sana: {formatted_date}\n"
            )
            await message.answer(text)

    except Exception as e:
        await message.answer(f"❌ Xatolik: {e}")


async def main():
    print("🤖 Bot ishga tushdi...")

    asyncio.create_task(realtime_checker())
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
