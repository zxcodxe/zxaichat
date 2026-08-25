# =======================================================
# ©️ 2026-27 ASTA
# Developer: @zxasta
# =======================================================

from pyrogram import filters
from pyrogram.types import (
    InlineKeyboardMarkup,
    InlineKeyboardButton,
    CallbackQuery,
    Message,
)

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
    bot_username = getattr(app, "username", None)

    if bot_username:
        bot_username = bot_username.lstrip("@")
        bot_link = f"https://t.me/{bot_username}"
        bot_display = f"[{bot_name}]({bot_link})"
    else:
        bot_display = bot_name

    return f"""
๏ ᴛʜɪs ɪs  ˹ {bot_display} ˼  🍃

➻ ᴀ ғᴀsᴛ & ᴘᴏᴡᴇʀғᴜʟ ᴀɪ ʙᴏᴛ

▸ 𝐀ɪ ᴄʜᴀᴛ • sᴍᴀʀᴛ ʀᴇsᴘᴏɴsᴇs 🤖
▸ 𝐒ᴇᴄᴜʀɪᴛʏ • ᴀɴᴛɪ-sᴘᴀᴍ ✨
▸ 𝐌ᴀɴᴀɢᴇ • ᴀᴜᴛᴏ-ʀᴇᴘʟʏ & ɴᴏᴛᴇs 🍃
────────────────────

๏ ᴘᴏᴡᴇʀᴇᴅ ʙʏ  ˹ ᴀsᴛᴀ ꭙ ꜱᴜᴘᴘᴏʀᴛ ˼
"""


# =======================================================
# MAIN BUTTONS
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
            ],
            [
                InlineKeyboardButton(
                    "˹ ᴅєᴠєʟσᴘєʀ ˼",
                    url="https://t.me/zxasta",
                ),
                InlineKeyboardButton(
                    "˹ ʟᴧηɢυᴧɢє ˼",
                    callback_data="language_panel",
                ),
            ],
            [
                InlineKeyboardButton(
                    "˹ ʜєʟᴘ ᴧηᴅ ᴄσϻϻᴧηᴅs ˼",
                    callback_data="help_panel",
                )
            ],
        ]
    )


# =======================================================
# HELP PANEL
# =======================================================

def get_help_text():
    return """
๏ ʜєʟᴘ & ᴄσϻϻᴧηᴅs 🤖

➻ ɢʀσυᴘ ᴄʜᴧᴛ

▸ ʜєʟʟσ ᴧɪ
   → Say "hello ai" in the group to chat with me.

▸ ϻєηᴛɪση
   → Mention me and send your message.

▸ ʀєᴘʟʏ
   → Reply to my message to continue chatting.

────────────────────

➻ ᴘʀɪᴠᴧᴛє ᴄʜᴧᴛ

▸ Send any message in private chat to talk with AI.

────────────────────

๏ ᴘσᴡєʀєᴅ ʙʏ  ˹ ᴀsᴛᴀ ꭙ ꜱᴜᴘᴘᴏʀᴛ ˼
"""


# =======================================================
# HELP BUTTONS
# =======================================================

def get_help_buttons():
    return InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    "‹ ʙᴧᴄᴋ",
                    callback_data="back_start",
                )
            ]
        ]
    )


# =======================================================
# LANGUAGE PANEL
# =======================================================

def get_language_text():
    return """
๏ ʟᴧηɢυᴧɢє sєʟєᴄᴛɪση 🌐

➻ Choose your preferred language.

Your selected language will be used for
the bot's panels, buttons and messages.
"""


# =======================================================
# LANGUAGE BUTTONS
# =======================================================

def get_language_buttons():
    return InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton("🇬🇧 English", callback_data="lang_en"),
                InlineKeyboardButton("🇮🇳 हिन्दी", callback_data="lang_hi"),
            ],
            [
                InlineKeyboardButton("🇵🇰 اردو", callback_data="lang_ur"),
                InlineKeyboardButton("🇸🇦 العربية", callback_data="lang_ar"),
            ],
            [
                InlineKeyboardButton("🇧🇩 বাংলা", callback_data="lang_bn"),
                InlineKeyboardButton("🇮🇳 தமிழ்", callback_data="lang_ta"),
            ],
            [
                InlineKeyboardButton(
                    "‹ ʙᴧᴄᴋ",
                    callback_data="back_start",
                )
            ],
        ]
    )


# =======================================================
# CALLBACK HANDLER
# =======================================================

@app.on_callback_query(
    filters.regex(
        r"^(help_panel|language_panel|back_start|lang_)"
    )
)
async def start_callback(client, query: CallbackQuery):

    data = query.data

    try:
        await query.answer()
    except Exception:
        pass

    # ---------------------------------------------------
    # HELP
    # ---------------------------------------------------

    if data == "help_panel":

        await query.message.edit_caption(
            caption=get_help_text(),
            reply_markup=get_help_buttons(),
        )

        return

    # ---------------------------------------------------
    # LANGUAGE
    # ---------------------------------------------------

    if data == "language_panel":

        await query.message.edit_caption(
            caption=get_language_text(),
            reply_markup=get_language_buttons(),
        )

        return

    # ---------------------------------------------------
    # BACK
    # ---------------------------------------------------

    if data == "back_start":

        await query.message.edit_caption(
            caption=get_start_text(),
            reply_markup=get_start_buttons(),
        )

        return

    # ---------------------------------------------------
    # LANGUAGE SELECTION
    # ---------------------------------------------------

    if data.startswith("lang_"):

        language = data.replace("lang_", "")

        # Temporary confirmation.
        # Full translation system can be connected
        # to database afterwards.

        names = {
            "en": "English 🇬🇧",
            "hi": "Hindi 🇮🇳",
            "ur": "Urdu 🇵🇰",
            "ar": "Arabic 🇸🇦",
            "bn": "Bengali 🇧🇩",
            "ta": "Tamil 🇮🇳",
        }

        selected = names.get(language, "English 🇬🇧")

        await query.answer(
            f"Language selected: {selected}",
            show_alert=False,
        )

        await query.message.edit_caption(
            caption=get_start_text(),
            reply_markup=get_start_buttons(),
        )

        return


# =======================================================
# /START
# =======================================================

@app.on_message(
    filters.command("start", prefixes="/")
)
async def start_command(client, message: Message):

    text = get_start_text()
    buttons = get_start_buttons()

    try:
        await message.reply_photo(
            photo=START_IMAGE,
            caption=text,
            reply_markup=buttons,
        )

    except Exception:
        try:
            await message.reply_text(
                text,
                reply_markup=buttons,
            )

        except Exception:
            pass


# =======================================================
# ©️ 2026-27 ASTA
# =======================================================
