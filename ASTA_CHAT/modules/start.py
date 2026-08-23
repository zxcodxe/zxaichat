# =======================================================
# ©️ 2026-27 ASTA
# Developer: @zxasta
# =======================================================

from pyrogram import filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message

from ASTA_CHAT import app


# =======================================================
# START TEXT
# =======================================================

def get_start_text():
    return f"""
**๏ ᴛʜɪs ɪs ˹ {app.name} ˼ 🍃**
**➻ ᴀ ғᴀsᴛ & ᴘᴏᴡᴇʀғᴜʟ ᴀɪ & ᴍᴀɴᴀɢᴇᴍᴇɴᴛ ʙᴏᴛ**
**▸ 𝐀ɪ ᴄʜᴀᴛ • sᴍᴀʀᴛ ʀᴇsᴘᴏɴsᴇs 🤖**
**▸ 𝐒ᴇᴄᴜʀɪᴛʏ • ᴀɴᴛɪ-sᴘᴀᴍ ✨**
**▸ 𝐌ᴀɴᴀɢᴇ • ᴀᴜᴛᴏ-ʀᴇᴘʟʏ & ɴᴏᴛᴇs 🍃**
**────────────────────**
**๏ ᴘᴏᴡᴇʀᴇᴅ ʙʏ [ᴀsᴛᴀ ꭙ ꜱᴜᴘᴘᴏʀᴛ](https://t.me/ixasta1)**
"""

# =======================================================
# START BUTTONS
# =======================================================

def get_start_buttons():
    return InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    "✚ ᴧᴅᴅ ϻᴇ ɪη ʏσυʀ ɢʀσυᴘ ✚",
                    url=f"https://t.me/{app.username}?startgroup=true",
                )
            ],
        ]
    )


# =======================================================
# /START
# =======================================================

@app.on_message(filters.command("start") & ~filters.bot)
async def start_command(client, message: Message):

    await message.reply_text(
        text=get_start_text(),
        reply_markup=get_start_buttons(),
        disable_web_page_preview=True,
    )


# =======================================================
# ©️ 2026-27 ASTA
# =======================================================
