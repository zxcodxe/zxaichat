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
๏ **ᴛʜɪs ɪs**  ˹ {bot_name} ˼  🍃

➻ **ᴀ ғᴀsᴛ & ᴘᴏᴡᴇʀғᴜʟ ᴀɪ ʙᴏᴛ**

▸ **𝐀ɪ ᴄʜᴀᴛ** • **sᴍᴀʀᴛ ʀᴇsᴘᴏɴsᴇs** 🤖
▸ **𝐒ᴇᴄᴜʀɪᴛʏ** • **ᴀɴᴛɪ-sᴘᴀᴍ** ✨
▸ **𝐌ᴀɴᴀɢᴇ** • **ᴀᴜᴛᴏ-ʀᴇᴘʟʏ & ɴᴏᴛᴇs** 🍃
────────────────────

๏ **ᴘᴏᴡᴇʀᴇᴅ ʙʏ**  [˹ ᴀsᴛᴀ ꭙ ꜱᴜᴘᴘᴏʀᴛ ˼](https://t.me/ixasta1)
""",

        "add": "✚ ᴧᴅᴅ ϻᴇ ɪη ʏσυʀ ɢʀσυᴘ ✚",
        "developer": "˹ ᴅєᴠєʟσᴘєʀ ˼",
        "language": "˹ ʟᴧηɢυᴧɢє ˼",
        "help_button": "˹ ʜєʟᴘ ᴧηᴅ ᴄσϻϻᴧηᴅs ˼",
        "back": "‹ ʙᴧᴄᴋ",

        "help": """
๏ **ʜєʟᴘ & ᴄσϻϻᴧηᴅs** 🤖

➻ **ɢʀσυᴘ ᴄʜᴧᴛ**

▸ **ʜєʟʟσ ᴧɪ**
   → Say "**hello ai**" in the group to chat with me.

▸ **ϻєηᴛɪση**
   → Mention me and send your message.

▸ **ʀєᴘʟʏ**
   → Reply to my message to continue chatting.

────────────────────

➻ **ᴘʀɪᴠᴧᴛє ᴄʜᴧᴛ**

▸ Send any message in private chat to talk with AI.

────────────────────

๏ **ᴘσᴡєʀєᴅ ʙʏ**  [˹ ᴀsᴛᴀ ꭙ ꜱᴜᴘᴘᴏʀᴛ ˼](https://t.me/ixasta1)
""",

        "language_title": "๏ **ʟᴧηɢυᴧɢє sєʟєᴄᴛɪση** 🌐",
        "language_text": """
➻ **Choose your preferred language.**

Your selected language will be used for
the bot's panels, buttons and messages.
""",

        "selected": "Language selected: {name}",
    },

    "hi": {
        "name": "हिन्दी 🇮🇳",

        "start": """
๏ **यह है**  ˹ {bot_name} ˼  🍃

➻ **एक तेज़ और शक्तिशाली AI बोट**

▸ **AI चैट** • **स्मार्ट उत्तर** 🤖
▸ **सुरक्षा** • **एंटी-स्पैम** ✨
▸ **प्रबंधन** • **ऑटो-रिप्लाई और नोट्स** 🍃
────────────────────

๏ **संचालित द्वारा**  [˹ ᴀsᴛᴀ ꭙ ꜱᴜᴘᴘᴏʀᴛ ˼](https://t.me/ixasta1)
""",

        "add": "✚ मुझे अपने ग्रुप में जोड़ें ✚",
        "developer": "˹ डेवलपर ˼",
        "language": "˹ भाषा ˼",
        "help_button": "˹ मदद और कमांड्स ˼",
        "back": "‹ वापस",

        "help": """
๏ **मदद और कमांड्स** 🤖

➻ **ग्रुप चैट**

▸ **हेलो AI**
   → ग्रुप में "**hello ai**" लिखकर मुझसे बात करें।

▸ **मेंशन**
   → मुझे मेंशन करके अपना मैसेज भेजें।

▸ **रिप्लाई**
   → मेरे मैसेज पर रिप्लाई करके बात करें।

────────────────────

➻ **प्राइवेट चैट**

▸ प्राइवेट चैट में कोई भी मैसेज भेजकर AI से बात करें।

────────────────────

๏ **संचालित द्वारा**  [˹ ᴀsᴛᴀ ꭙ ꜱᴜᴘᴘᴏʀᴛ ˼](https://t.me/ixasta1)
""",

        "language_title": "๏ **भाषा का चयन करें** 🌐",
        "language_text": """
➻ **अपनी पसंदीदा भाषा चुनें।**

आपकी चुनी हुई भाषा बोट के पैनल,
बटन और संदेशों में उपयोग की जाएगी।
""",

        "selected": "चयनित भाषा: {name}",
    },

    "ur": {
        "name": "اردو 🇵🇰",

        "start": """
๏ **یہ ہے**  ˹ {bot_name} ˼  🍃

➻ **ایک تیز اور طاقتور AI بوٹ**

▸ **AI چیٹ** • **سمارٹ جوابات** 🤖
▸ **سیکیورٹی** • **اینٹی سپیم** ✨
▸ **انتظام** • **خودکار جواب اور نوٹس** 🍃
────────────────────

๏ **پاورڈ بائی**  [˹ ᴀsᴛᴀ ꭙ ꜱᴜᴘᴘᴏʀᴛ ˼](https://t.me/ixasta1)
""",

        "add": "✚ مجھے اپنے گروپ میں شامل کریں ✚",
        "developer": "˹ ڈیولپر ˼",
        "language": "˹ زبان ˼",
        "help_button": "˹ مدد اور کمانڈز ˼",
        "back": "‹ واپس",

        "help": """
๏ **مدد اور کمانڈز** 🤖

➻ **گروپ چیٹ**

▸ **ہیلو AI**
   → گروپ میں "**hello ai**" لکھ کر مجھ سے بات کریں۔

▸ **مینشن**
   → مجھے مینشن کر کے اپنا پیغام بھیجیں۔

▸ **ریپلائی**
   → میرے پیغام کا جواب دے کر بات جاری رکھیں۔

────────────────────

➻ **پرائیویٹ چیٹ**

▸ پرائیویٹ چیٹ میں کوئی بھی پیغام بھیج کر AI سے بات کریں۔

────────────────────

๏ **پاورڈ بائی**  [˹ ᴀsᴛᴀ ꭙ ꜱᴜᴘᴘᴏʀᴛ ˼](https://t.me/ixasta1)
""",

        "language_title": "๏ **زبان کا انتخاب** 🌐",
        "language_text": """
➻ **اپنی پسندیدہ زبان منتخب کریں۔**

آپ کی منتخب کردہ زبان بوٹ کے پینل،
بٹن اور پیغامات میں استعمال ہوگی۔
""",

        "selected": "منتخب کردہ زبان: {name}",
    },

    "ar": {
        "name": "العربية 🇸🇦",

        "start": """
๏ **هذا هو**  ˹ {bot_name} ˼  🍃

➻ **بوت ذكاء اصطناعي سريع وقوي**

▸ **دردشة الذكاء الاصطناعي** • **إجابات ذكية** 🤖
▸ **الأمان** • **مكافحة السبام** ✨
▸ **الإدارة** • **الرد التلقائي والملاحظات** 🍃
────────────────────

๏ **بواسطة**  [˹ ᴀsᴛᴀ ꭙ ꜱᴜᴘᴘᴏʀᴛ ˼](https://t.me/ixasta1)
""",

        "add": "✚ أضفني إلى مجموعتك ✚",
        "developer": "˹ المطور ˼",
        "language": "˹ اللغة ˼",
        "help_button": "˹ المساعدة والأوامر ˼",
        "back": "‹ عودة",

        "help": """
๏ **المساعدة والأوامر** 🤖

➻ **المحادثة الجماعية**

▸ **مرحباً AI**
   → اكتب "**hello ai**" في المجموعة للتحدث معي.

▸ **الإشارة (Mention)**
   → قم بالإشارة إلي وأرسل رسالتك.

▸ **الرد (Reply)**
   → قم بالرد على رسالتي لمواصلة المحادثة.

────────────────────

➻ **المحادثة الخاصة**

▸ أرسل أي رسالة في المحادثة الخاصة للتحدث مع الذكاء الاصطناعي.

────────────────────

๏ **بواسطة**  [˹ ᴀsᴛᴀ ꭙ ꜱᴜᴘᴘᴏʀᴛ ˼](https://t.me/ixasta1)
""",

        "language_title": "๏ **اختيار اللغة** 🌐",
        "language_text": """
➻ **اختر لغتك المفضلة.**

ستُستخدم اللغة المحددة في
لوحات البوت والأزرار والرسائل.
""",

        "selected": "اللغة المختارة: {name}",
    },

    "bn": {
        "name": "বাংলা 🇧🇩",

        "start": """
๏ **এটি হলো**  ˹ {bot_name} ˼  🍃

➻ **একটি দ্রুত এবং শক্তিশালী AI বোট**

▸ **AI চ্যাট** • **স্মার্ট উত্তর** 🤖
▸ **নিরাপত্তা** • **অ্যান্টি-স্প্যাম** ✨
▸ **ব্যবস্থাপনা** • **অটো-রিপ্লাই এবং নোট** 🍃
────────────────────

๏ **পাওয়ার্ড বাই**  [˹ ᴀsᴛᴀ ꭙ ꜱᴜᴘᴘᴏʀᴛ ˼](https://t.me/ixasta1)
""",

        "add": "✚ আমাকে আপনার গ্রুপে যোগ করুন ✚",
        "developer": "˹ ডেভেলপার ˼",
        "language": "˹ ভাষা ˼",
        "help_button": "˹ সাহায্য এবং কমান্ড ˼",
        "back": "‹ পিছনে",

        "help": """
๏ **সাহায্য এবং কমান্ড** 🤖

➻ **গ্রুপ চ্যাট**

▸ **হ্যালো AI**
   → গ্রুপে "**hello ai**" লিখে আমার সাথে কথা বলুন।

▸ **মেনশন**
   → আমাকে মেনশন করে আপনার মেসেজ পাঠান।

▸ **রিপ্লাই**
   → আমার মেসেজে রিপ্লাই করে কথা বলুন।

────────────────────

➻ **প্রাইভেট চ্যাট**

▸ প্রাইভেট চ্যাটে মেসেজ পাঠিয়ে AI-এর সাথে কথা বলুন।

────────────────────

๏ **পাওয়ার্ড বাই**  [˹ ᴀsᴛᴀ ꭙ ꜱᴜᴘᴘᴏʀᴛ ˼](https://t.me/ixasta1)
""",

        "language_title": "๏ **ভাষা নির্বাচন** 🌐",
        "language_text": """
➻ **আপনার পছন্দের ভাষা নির্বাচন করুন।**

নির্বাচিত ভাষাটি বোটের প্যানেল,
বাটন এবং মেসেজে ব্যবহার করা হবে।
""",

        "selected": "নির্বাচিত ভাষা: {name}",
    },

    "ta": {
        "name": "தமிழ் 🇮🇳",

        "start": """
๏ **இது**  ˹ {bot_name} ˼  🍃

➻ **ஒரு வேகமான & சக்திவாய்ந்த AI போட்**

▸ **AI சேட்** • **ஸ்மார்ட் பதில்கள்** 🤖
▸ **பாதுகாப்பு** • **ஆண்டி-ஸ்பேம்** ✨
▸ **நிர்வகிப்பு** • **ஆட்டோ-ரிப்ளை & குறிப்புகள்** 🍃
────────────────────

๏ **இயக்குபவர்**  [˹ ᴀsᴛᴀ ꭙ ꜱᴜᴘᴘᴏʀᴛ ˼](https://t.me/ixasta1)
""",

        "add": "✚ என்னை ඔබේ குழுவில் சேர்க்கவும் ✚",
        "developer": "˹ உருவாக்குநர் ˼",
        "language": "˹ மொழி ˼",
        "help_button": "˹ உதவி & கட்டளைகள் ˼",
        "back": "‹ பின்செல்",

        "help": """
๏ **உதவி & கட்டளைகள்** 🤖

➻ **குழு சேட்**

▸ **ஹலோ AI**
   → குழுவில் "**hello ai**" என்று தட்டச்சு செய்து என்னுடன் பேசுங்கள்.

▸ **மென்ஷன்**
   → என்னை மென்ஷன் செய்து உங்கள் செய்தியை அனுப்புங்கள்.

▸ **பதில் (Reply)**
   → என் செய்திக்கு பதில் அளித்து உரையாடலைத் தொடருங்கள்.

────────────────────

➻ **தனிப்பட்ட சேட்**

▸ தனிப்பட்ட சேட்டில் செய்தி அனுப்பி AI உடன் பேசுங்கள்.

────────────────────

๏ **இயக்குபவர்**  [˹ ᴀsᴛᴀ ꭙ ꜱᴜᴘᴘᴏʀᴛ ˼](https://t.me/ixasta1)
""",

        "language_title": "๏ **மொழி தேர்வு** 🌐",
        "language_text": """
➻ **உங்களுக்கு விருப்பமான மொழியைத் தேர்ந்தெடுக்கவும்.**

தேர்ந்தெடுக்கப்பட்ட மொழி போட்டின் பேனல்கள்,
பட்டன்கள் மற்றும் செய்திகளில் பயன்படுத்தப்படும்.
""",

        "selected": "தேர்ந்தெடுக்கப்பட்ட மொழி: {name}",
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
    ),
    group=-1,
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
