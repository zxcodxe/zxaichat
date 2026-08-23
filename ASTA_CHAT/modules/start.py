# =======================================================
# ©️ 2026-27 ASTA
# Developer: @zxasta
# =======================================================

from pyrogram import filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message

from ASTA_CHAT import app


# =======================================================
# START IMAGE
# =======================================================

START_IMAGE = (
    "https://graph.org/file/"
    "9bdf36b86a38660129902-d9b13eebf332fb6b0e.jpg"
)


# =======================================================
# START TEXT
# =======================================================

def get_start_text():
    bot_name = getattr(app, "name", None) or "Zenithaibot"

    return f"""
**๏ ᴛʜɪs ɪs   {bot_name}   🍃**

**➻ ᴀ ғᴀsᴛ & ᴘᴏᴡᴇʀғᴜʟ ᴀɪ & ᴍᴀɴᴀɢᴇᴍᴇɴᴛ ʙᴏᴛ**

**▸ 𝐀ɪ ᴄʜᴀᴛ • sᴍᴀʀᴛ ʀᴇsᴘᴏɴsᴇs 🤖**
**▸ 𝐒ᴇᴄᴜʀɪᴛʏ • ᴀɴᴛɪ-sᴘᴀᴍ ✨**
**▸ 𝐌ᴀɴᴀɢᴇ • ᴀᴜᴛᴏ-ʀᴇᴘʟʏ & ɴᴏᴛᴇs 🍃**
**────────────────────**
"""


# =======================================================
# START BUTTONS
# =======================================================

def get_start_buttons():
    bot_username = getattr(app, "username", None)

    if not bot_username:
        return None

    bot_username = bot_username.lstrip("@")

    return InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    "✚ ᴧᴅᴅ ϻᴇ ɪη ʏσυʀ ɢʀσυᴘ ✚",
                    url=f"https://t.me/{bot_username}?startgroup=true",
                )
            ]
        ]
    )


# =======================================================
# /START
# =======================================================

@app.on_message(filters.command("start"))
async def start_command(client, message: Message):

    await message.reply_photo(
        photo=START_IMAGE,
        caption=get_start_text(),
        reply_markup=get_start_buttons(),
    )


# =======================================================
# ©️ 2026-27 ASTA
# =======================================================
