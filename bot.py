from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo
from config import *
from database import add_user, get_users

app = Client(
    "bot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)

@app.on_message(filters.command("start"))
async def start(client, message):
    user_id = message.from_user.id
    add_user(user_id)

    keyboard = InlineKeyboardMarkup([
        [InlineKeyboardButton("🎁 OPEN", web_app=WebAppInfo(url=WEB_URL))]
    ])

    await client.send_video(
    user_id,
    video="https://res.cloudinary.com/dbppv000g/video/upload/v1776889834/SLOT138_ovtiud.mp4",
    caption="🔥 Gameplay gacor hari ini!"
)

    await client.send_voice(
        user_id,
        voice="https://www2.cs.uic.edu/~i101/SoundFiles/StarWars60.wav"
    )

    await message.reply_text(
        f"Hello {message.from_user.first_name}\n\nBot VIP aktif 🎁",
        reply_markup=keyboard
    )


@app.on_message(filters.command("bc") & filters.user(ADMINS))
async def broadcast(client, message):
    if not message.reply_to_message:
        return await message.reply("Reply pesan!")

    users = get_users()
    sukses = 0

    for user in users:
        try:
            await message.reply_to_message.copy(user)
            sukses += 1
        except:
            pass

    await message.reply(f"Done {sukses}/{len(users)}")


app.run()
