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
from ASTA_CHAT.database.chatbot import (
    get_user_language,
    set_user_language,
)


# =======================================================
# START IMAGE
# =======================================================

START_IMAGE = (
    "https://graph.org/file/"
    "9bdf36b86a38660129902-d9b13eebf332fb6b0e.jpg"
)


# =======================================================
# TRANSLATIONS
# =======================================================

LANGUAGES = {
    "en": {
        "name": "English 🇬🇧",

        "start": """
๏ ᴛʜɪs ɪs  ˹ {bot_name} ˼  🍃

➻ ᴀ ғᴀsᴛ & ᴘᴏᴡᴇʀғᴜʟ ᴀɪ ʙᴏᴛ

▸ 𝐀ɪ ᴄʜᴀᴛ • sᴍᴀʀᴛ ʀᴇsᴘᴏɴsᴇs 🤖
▸ 𝐒ᴇᴄᴜʀɪᴛʏ • ᴀɴᴛɪ-sᴘᴀᴍ ✨
▸ 𝐌ᴀɴᴀɢᴇ • ᴀᴜᴛᴏ-ʀᴇᴘʟʏ & ɴᴏᴛᴇs 🍃
────────────────────

๏ ᴘᴏᴡᴇʀᴇᴅ ʙʏ  ˹ ᴀsᴛᴀ ꭙ ꜱᴜᴘᴘᴏʀᴛ ˼
""",

        "add": "✚ ᴧᴅᴅ ϻᴇ ɪη ʏσυʀ ɢʀσυᴘ ✚",
        "developer": "˹ ᴅєᴠєʟσᴘєʀ ˼",
        "language": "˹ ʟᴧηɢυᴧɢє ˼",
        "help_button": "˹ ʜєʟᴘ ᴧηᴅ ᴄσϻϻᴧηᴅs ˼",
        "back": "‹ ʙᴧᴄᴋ",

        "help": """
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
""",

        "language_title": "๏ ʟᴧηɢυᴧɢє sєʟєᴄᴛɪση 🌐",
        "language_text": """
➻ Choose your preferred language.

Your selected language will be used for
the bot's panels, buttons and messages.
""",

        "selected": "Language selected: {name}",
    },

    "hi": {
        "name": "हिन्दी 🇮🇳",

        "start": """
๏ ʏє ʜᴇɪ  ˹ {bot_name} ˼  🍃

➻ ᴇᴋ ғᴀsᴛ & ᴘᴏᴡᴇʀғᴜʟ ᴀɪ ʙᴏᴛ

▸ 𝐀ɪ ᴄʜᴀᴛ • sᴍᴀʀᴛ ʀᴇsᴘᴏɴsᴇs 🤖
▸ 𝐒ᴇᴄᴜʀɪᴛʏ • ᴀɴᴛɪ-sᴘᴀᴍ ✨
▸ 𝐌ᴀɴᴀɢᴇ • ᴀᴜᴛᴏ-ʀᴇᴘʟʏ & ɴᴏᴛᴇs 🍃
────────────────────

๏ ᴘᴏᴡᴇʀᴇᴅ ʙʏ  ˹ ᴀsᴛᴀ ꭙ ꜱᴜᴘᴘᴏʀᴛ ˼
""",

        "add": "✚ ᴀᴘɴᴇ ɢʀᴏᴜᴘ ᴍᴇɪɴ ᴍᴜᴊʜᴇ ᴀᴅᴅ ᴋᴀʀᴇɪɴ ✚",
        "developer": "˹ ᴅᴇᴠᴇʟᴏᴘᴇʀ ˼",
        "language": "˹ ʙʜᴀsʜᴀ ˼",
        "help_button": "˹ ʜᴇʟᴘ & ᴋᴏᴍᴀɴᴅs ˼",
        "back": "‹ ᴠᴀᴘᴀs",

        "help": """
๏ ʜᴇʟᴘ & ᴋᴏᴍᴀɴᴅs 🤖

➻ ɢʀᴏᴜᴘ ᴄʜᴀᴛ

▸ ʜᴇʟʟᴏ ᴀɪ
   → Group mein "hello ai" likhkar mujhse baat karein.

▸ ᴍᴇɴᴛɪᴏɴ
   → Mujhe mention karke apna message bhejein.

▸ ʀᴇᴘʟʏ
   → Mere message par reply karke baat karein.

────────────────────

➻ ᴘʀɪᴠᴀᴛᴇ ᴄʜᴀᴛ

▸ Private chat mein koi bhi message bhejkar AI se baat karein.

────────────────────

๏ ᴘᴏᴡᴇʀᴇᴅ ʙʏ  ˹ ᴀsᴛᴀ ꭙ ꜱᴜᴘᴘᴏʀᴛ ˼
""",

        "language_title": "๏ ʙʜᴀsʜᴀ ᴄʜᴜɴᴇɪɴ 🌐",
        "language_text": """
➻ Apni pasand ki bhasha select karein.

Aapki selected language bot ke panels,
buttons aur messages mein use hogi.
""",

        "selected": "Language selected: {name}",
    },

    "ur": {
        "name": "اردو 🇵🇰",

        "start": """
๏ ʏᴇʜ ʜᴀɪ ˹ {bot_name} ˼ 🍃

➻ ᴇᴋ ғᴀsᴛ & ᴘᴏᴡᴇʀғᴜʟ ᴀɪ ʙᴏᴛ

▸ 𝐀ɪ ᴄʜᴀᴛ • sᴍᴀʀᴛ ʀᴇsᴘᴏɴsᴇs 🤖
▸ 𝐒ᴇᴄᴜʀɪᴛʏ • ᴀɴᴛɪ-sᴘᴀᴍ ✨
▸ 𝐌ᴀɴᴀɢᴇ • ᴀᴜᴛᴏ-ʀᴇᴘʟʏ & ɴᴏᴛᴇs 🍃
────────────────────

๏ ᴘᴏᴡᴇʀᴇᴅ ʙʏ  ˹ ᴀsᴛᴀ ꭙ ꜱᴜᴘᴘᴏʀᴛ ˼
""",

        "add": "✚ ᴍᴜᴊʜᴇ ᴀᴘɴᴇ ɢʀᴏᴜᴘ ᴍᴇɪɴ ᴀᴅᴅ ᴋᴀʀᴇɪɴ ✚",
        "developer": "˹ ᴅᴇᴠᴇʟᴏᴘᴇʀ ˼",
        "language": "˹ ᴢᴀʙᴀɴ ˼",
        "help_button": "˹ ʜᴇʟᴘ & ᴋᴏᴍᴀɴᴅs ˼",
        "back": "‹ ᴡᴀᴘɪs",

        "help": """
๏ ʜᴇʟᴘ & ᴋᴏᴍᴀɴᴅs 🤖

➻ ɢʀᴏᴜᴘ ᴄʜᴀᴛ

▸ ʜᴇʟʟᴏ ᴀɪ
   → Group mein "hello ai" likh kar mujhse baat karein.

▸ ᴍᴇɴᴛɪᴏɴ
   → Mujhe mention karke apna message bhejein.

▸ ʀᴇᴘʟʏ
   → Mere message par reply karke baat karein.

────────────────────

➻ ᴘʀɪᴠᴀᴛᴇ ᴄʜᴀᴛ

▸ Private chat mein message bhej kar AI se baat karein.

────────────────────

๏ ᴘᴏᴡᴇʀᴇᴅ ʙʏ  ˹ ᴀsᴛᴀ ꭙ sᴜᴘᴘᴏʀᴛ ˼
""",

        "language_title": "๏ ᴢᴀʙᴀɴ ᴋᴀ ɪɴᴛɪᴋʜᴀʙ 🌐",
        "language_text": """
➻ Apni pasand ki zaban select karein.

Aapki selected zaban bot ke panels,
buttons aur messages mein use hogi.
""",

        "selected": "Language selected: {name}",
    },

    "ar": {
        "name": "العربية 🇸🇦",

        "start": """
๏ ʜᴀᴅʜᴀ ˹ {bot_name} ˼ 🍃

➻ ʙᴏᴛ ᴀɪ sᴀʀɪᴇᴄ ᴡᴀ ᴘᴏᴡᴇʀғᴜʟ

▸ 𝐀ɪ ᴄʜᴀᴛ • sᴍᴀʀᴛ ʀᴇsᴘᴏɴsᴇs 🤖
▸ 𝐒ᴇᴄᴜʀɪᴛʏ • ᴀɴᴛɪ-sᴘᴀᴍ ✨
▸ 𝐌ᴀɴᴀɢᴇ • ᴀᴜᴛᴏ-ʀᴇᴘʟʏ & ɴᴏᴛᴇs 🍃
────────────────────

๏ ᴘᴏᴡᴇʀᴇᴅ ʙʏ  ˹ ᴀsᴛᴀ ꭙ sᴜᴘᴘᴏʀᴛ ˼
""",

        "add": "✚ ᴍʏ ᴜᴘᴅᴀᴅ ᴛᴏ ɢʀᴏᴜᴘ ✚",
        "developer": "˹ ᴅᴇᴠᴇʟᴏᴘᴇʀ ˼",
        "language": "˹ ʟᴜɢʜᴀ ˼",
        "help_button": "˹ ᴍᴜsᴀᴀᴅᴀ & ᴋᴏᴍᴀɴᴅᴜᴛ ˼",
        "back": "‹ ʀᴜᴊᴜᴜ",

        "help": """
๏ ᴍᴜsᴀᴀᴅᴀ & ᴋᴏᴍᴀɴᴅᴜᴛ 🤖

➻ ᴍᴜʜᴀᴅᴀᴛʜᴀᴛ ᴀʟᴍᴜᴊᴍᴜᴜᴀ

▸ ʜᴇʟʟᴏ ᴀɪ
   → ᴜᴋᴛᴜʙ "hello ai" ʟɪᴛᴀʜᴀᴅᴅᴀᴛʜ ᴍᴀʟᴇᴇ.

▸ ᴍᴇɴᴛɪᴏɴ
   → ᴀᴫᴋᴜʀ ᴍᴇɴᴛɪᴏɴ ʟɪʟʙᴏᴛ ᴡᴀᴛᴋᴜʙ ʀɪsᴀʟᴀᴛᴀᴋ.

▸ ʀᴇᴘʟʏ
   → ʀᴜᴅᴅ ᴀʟᴀ ʀɪsᴀʟᴀᴛ ᴀʟʙᴏᴛ ʟɪᴍᴜᴛᴀʙᴀᴀᴛᴀ.

────────────────────

➻ ᴍᴜʜᴀᴅᴀᴛʜᴀ ᴋʜᴀᴀs

▸ ᴀʀsᴀʟ ᴀʏʏ ʀɪsᴀʟᴀ ʟɪʟᴅʜᴇʙᴀᴛ ᴍᴜʜᴀᴅᴀᴛʜᴀ.

────────────────────

๏ ᴘᴏᴡᴇʀᴇᴅ ʙʏ  ˹ ᴀsᴛᴀ ꭙ sᴜᴘᴘᴏʀᴛ ˼
""",

        "language_title": "๏ ɪᴋʜᴛɪʏᴀʀ ʟᴜɢʜᴀ 🌐",
        "language_text": """
➻ ɪᴋʜᴛᴀʀ ʟᴜɢʜᴀ ᴀʟʟᴀᴛɪ ᴛᴜғᴀᴅᴅʜɪʟᴜʜᴀ.

sᴀʏᴀᴛᴇᴍ ɪsᴛᴋʜᴅᴀᴍ ʟᴜɢʜᴀᴛᴋ
ғɪ ᴋᴜʟ ᴀʟᴘᴀᴡᴀʙᴀᴛ ᴡᴀʟᴀᴢʀᴀʀ.
""",

        "selected": "Language selected: {name}",
    },

    "bn": {
        "name": "বাংলা 🇧🇩",

        "start": """
๏ ᴇɪ ʜᴏʟᴏ ˹ {bot_name} ˼ 🍃

➻ ᴇᴋᴛɪ ғᴀsᴛ & ᴘᴏᴡᴇʀғᴜʟ ᴀɪ ʙᴏᴛ

▸ 𝐀ɪ ᴄʜᴀᴛ • sᴍᴀʀᴛ ʀᴇsᴘᴏɴsᴇs 🤖
▸ 𝐒ᴇᴄᴜʀɪᴛʏ • ᴀɴᴛɪ-sᴘᴀᴍ ✨
▸ 𝐌ᴀɴᴀɢᴇ • ᴀᴜᴛᴏ-ʀᴇᴘʟʏ & ɴᴏᴛᴇs 🍃
────────────────────

๏ ᴘᴏᴡᴇʀᴇᴅ ʙʏ  ˹ ᴀsᴛᴀ ꭙ sᴜᴘᴘᴏʀᴛ ˼
""",

        "add": "✚ ᴀᴍᴀᴋᴇ ɢʀᴜᴘᴇ ʏᴏɢ ᴋᴏʀᴜɴ ✚",
        "developer": "˹ ᴅᴇᴠᴇʟᴏᴘᴇʀ ˼",
        "language": "˹ ʙʜᴀsʜᴀ ˼",
        "help_button": "˹ ʜᴇʟᴘ & ᴋᴏᴍᴀɴᴅs ˼",
        "back": "‹ ʙᴀᴄᴋ",

        "help": """
๏ ʜᴇʟᴘ & ᴋᴏᴍᴀɴᴅs 🤖

➻ ɢʀᴜᴘ ᴄʜᴀᴛ

▸ ʜᴇʟʟᴏ ᴀɪ
   → Group-e "hello ai" likhe bot-er sathe kotha bolun.

▸ ᴍᴇɴᴛɪᴏɴ
   → Bot-ke mention kore message pathan.

▸ ʀᴇᴘʟʏ
   → Bot-er message-e reply kore kotha bolun.

────────────────────

➻ ᴘʀɪᴠᴀᴛᴇ ᴄʜᴀᴛ

▸ Private chat-e message pathiye AI-er sathe kotha bolun.

────────────────────

๏ ᴘᴏᴡᴇʀᴇᴅ ʙʏ  ˹ ᴀsᴛᴀ ꭙ sᴜᴘᴘᴏʀᴛ ˼
""",

        "language_title": "๏ ʙʜᴀsʜᴀ ɴɪʀʙᴀᴄʜᴏɴ 🌐",
        "language_text": """
➻ Apnar pochonder bhasha nirbachon korun.

Selected bhasha bot-er panel,
button ebong message-e use hobe.
""",

        "selected": "Language selected: {name}",
    },

    "ta": {
        "name": "தமிழ் 🇮🇳",

        "start": """
๏ ɪᴅʜᴜ ˹ {bot_name} ˼ 🍃

➻ ᴏʀᴜ ғᴀsᴛ & ᴘᴏᴡᴇʀғᴜʟ ᴀɪ ʙᴏᴛ

▸ 𝐀ɪ ᴄʜᴀᴛ • sᴍᴀʀᴛ ʀᴇsᴘᴏɴsᴇs 🤖
▸ 𝐒ᴇᴄᴜʀɪᴛʏ • ᴀɴᴛɪ-sᴘᴀᴍ ✨
▸ 𝐌ᴀɴᴀɢᴇ • ᴀᴜᴛᴏ-ʀᴇᴘʟʏ & ɴᴏᴛᴇs 🍃
────────────────────

๏ ᴘᴏᴡᴇʀᴇᴅ ʙʏ  ˹ ᴀsᴛᴀ ꭙ sᴜᴘᴘᴏʀᴛ ˼
""",

        "add": "✚ ᴇɴ ɢʀᴏᴜᴘ-ɪʟ ᴇɴɴᴀɪ sᴇʀᴛʜᴜ ᴋᴏʟʟᴀᴠᴜᴍ ✚",
        "developer": "˹ ᴅᴇᴠᴇʟᴏᴘᴇʀ ˼",
        "language": "˹ ᴍᴏᴢʜɪ ˼",
        "help_button": "˹ ʜᴇʟᴘ & ᴋᴏᴍᴀɴᴅs ˼",
        "back": "‹ ᴛʜɪʀᴜᴍʙᴀ",

        "help": """
๏ ʜᴇʟᴘ & ᴋᴏᴍᴀɴᴅs 🤖

➻ ɢʀᴏᴜᴘ ᴄʜᴀᴛ

▸ ʜᴇʟʟᴏ ᴀɪ
   → Group-il "hello ai" endru type seithu pesa mudiyum.

▸ ᴍᴇɴᴛɪᴏɴ
   → Bot-ai mention seithu message anuppungal.

▸ ʀᴇᴘʟʏ
   → Bot message-ku reply seithu pesa mudiyum.

────────────────────

➻ ᴘʀɪᴠᴀᴛᴇ ᴄʜᴀᴛ

▸ Private chat-il message anuppi AI-udan pesungal.

────────────────────

๏ ᴘᴏᴡᴇʀᴇᴅ ʙʏ  ˹ ᴀsᴛᴀ ꭙ sᴜᴘᴘᴏʀᴛ ˼
""",

        "language_title": "๏ ᴍᴏᴢʜɪ ᴛᴇʀɴᴛʜᴇᴅᴜᴋᴋᴀ 🌐",
        "language_text": """
➻ Ungalukku piditha mozhiyaith therndhedungal.

Therndhedutha mozhi bot-in panels,
buttons matrum messages-il payanpadum.
""",

        "selected": "Language selected: {name}",
    },
}


# =======================================================
# LANGUAGE DATA
# =======================================================

def get_language_data(language: str):
    return LANGUAGES.get(
        language,
        LANGUAGES["en"],
    )


# =======================================================
# BOT INFORMATION
# =======================================================

def get_bot_info():
    bot_name = getattr(
        app,
        "name",
        None,
    ) or "Zenithaibot"

    bot_username = getattr(
        app,
        "username",
        None,
    )

    if bot_username:
        bot_username = bot_username.lstrip("@")

    return bot_name, bot_username


# =======================================================
# START TEXT
# =======================================================

async def get_start_text(user_id: int):
    language = await get_user_language(user_id)
    data = get_language_data(language)

    bot_name, bot_username = get_bot_info()

    if bot_username:
        bot_link = f"https://t.me/{bot_username}"
        bot_display = f"[{bot_name}]({bot_link})"
    else:
        bot_display = bot_name

    return data["start"].format(
        bot_name=bot_display
    )


# =======================================================
# MAIN BUTTONS
# =======================================================

async def get_start_buttons(user_id: int):

    language = await get_user_language(user_id)
    data = get_language_data(language)

    _, bot_username = get_bot_info()

    if not bot_username:
        return None

    return InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    data["add"],
                    url=(
                        f"https://t.me/"
                        f"{bot_username}"
                        f"?startgroup=true"
                    ),
                )
            ],
            [
                InlineKeyboardButton(
                    data["developer"],
                    url="https://t.me/zxasta",
                ),
                InlineKeyboardButton(
                    data["language"],
                    callback_data="language_panel",
                ),
            ],
            [
                InlineKeyboardButton(
                    data["help_button"],
                    callback_data="help_panel",
                )
            ],
        ]
    )


# =======================================================
# HELP TEXT
# =======================================================

async def get_help_text(user_id: int):

    language = await get_user_language(user_id)
    data = get_language_data(language)

    return data["help"]


# =======================================================
# HELP BUTTONS
# =======================================================

async def get_help_buttons(user_id: int):

    language = await get_user_language(user_id)
    data = get_language_data(language)

    return InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    data["back"],
                    callback_data="back_start",
                )
            ]
        ]
    )


# =======================================================
# LANGUAGE PANEL
# =======================================================

async def get_language_text(user_id: int):

    language = await get_user_language(user_id)
    data = get_language_data(language)

    return (
        data["language_title"]
        + "\n"
        + data["language_text"]
    )


# =======================================================
# LANGUAGE BUTTONS
# =======================================================

async def get_language_buttons(user_id: int):

    language = await get_user_language(user_id)
    data = get_language_data(language)

    return InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    "🇬🇧 English",
                    callback_data="lang_en",
                ),
                InlineKeyboardButton(
                    "🇮🇳 हिन्दी",
                    callback_data="lang_hi",
                ),
            ],
            [
                InlineKeyboardButton(
                    "🇵🇰 اردو",
                    callback_data="lang_ur",
                ),
                InlineKeyboardButton(
                    "🇸🇦 العربية",
                    callback_data="lang_ar",
                ),
            ],
            [
                InlineKeyboardButton(
                    "🇧🇩 বাংলা",
                    callback_data="lang_bn",
                ),
                InlineKeyboardButton(
                    "🇮🇳 தமிழ்",
                    callback_data="lang_ta",
                ),
            ],
            [
                InlineKeyboardButton(
                    data["back"],
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
async def start_callback(
    client,
    query: CallbackQuery,
):

    data = query.data
    user_id = query.from_user.id

    # ---------------------------------------------------
    # HELP
    # ---------------------------------------------------

    if data == "help_panel":

        await query.answer()

        await query.message.edit_caption(
            caption=await get_help_text(user_id),
            reply_markup=await get_help_buttons(user_id),
        )

        return

    # ---------------------------------------------------
    # LANGUAGE PANEL
    # ---------------------------------------------------

    if data == "language_panel":

        await query.answer()

        await query.message.edit_caption(
            caption=await get_language_text(user_id),
            reply_markup=await get_language_buttons(user_id),
        )

        return

    # ---------------------------------------------------
    # BACK
    # ---------------------------------------------------

    if data == "back_start":

        await query.answer()

        await query.message.edit_caption(
            caption=await get_start_text(user_id),
            reply_markup=await get_start_buttons(user_id),
        )

        return

    # ---------------------------------------------------
    # LANGUAGE SELECTION
    # ---------------------------------------------------

    if data.startswith("lang_"):

        language = data.replace(
            "lang_",
            "",
            1,
        )

        if language not in LANGUAGES:
            await query.answer(
                "Invalid language.",
                show_alert=True,
            )
            return

        # Save selected language in MongoDB.
        saved = await set_user_language(
            user_id,
            language,
        )

        if not saved:
            await query.answer(
                "Unable to save language.",
                show_alert=True,
            )
            return

        selected = LANGUAGES[language]["name"]

        await query.answer(
            LANGUAGES[language]["selected"].format(
                name=selected
            ),
            show_alert=False,
        )

        # Immediately show the main panel
        # in the newly selected language.
        await query.message.edit_caption(
            caption=await get_start_text(user_id),
            reply_markup=await get_start_buttons(user_id),
        )

        return


# =======================================================
# /START
# =======================================================

@app.on_message(
    filters.command(
        "start",
        prefixes="/",
    )
)
async def start_command(
    client,
    message: Message,
):

    user_id = message.from_user.id

    text = await get_start_text(user_id)
    buttons = await get_start_buttons(user_id)

    try:
        await message.reply_photo(
            photo=START_IMAGE,
            caption=text,
            reply_markup=buttons,
        )

    except Exception as e:

        print(
            f"[START] Photo failed: {type(e).__name__}: {e}"
        )

        try:
            await message.reply_text(
                text,
                reply_markup=buttons,
            )

        except Exception as e2:

            print(
                f"[START] Text failed: {type(e2).__name__}: {e2}"
            )
