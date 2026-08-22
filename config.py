# =======================================================
# ©️ 2026-27 All Rights Reserved by ASTA (ASTA) 🚀
#
# This source code is under MIT License 📜
# Unauthorized forking, importing, or using this code without
# giving proper credit will result in legal action ⚠️
#
# 📩 DM for permission : @zxasta
# =======================================================

from os import getenv
import os

from dotenv import load_dotenv

load_dotenv()


# ==========================================================
# TELEGRAM CONFIGURATION
# ==========================================================

API_ID = int(
    getenv(
        "API_ID",
        "23156684"
    )
)

API_HASH = getenv(
    "API_HASH",
    None
)

BOT_TOKEN = getenv(
    "BOT_TOKEN",
    None
)

OWNER_ID = 7808531413


# ==========================================================
# DATABASE
# ==========================================================

MONGO_URL = getenv(
    "MONGO_URL",
    None
)


# ==========================================================
# FORCE SUBSCRIBE
# ==========================================================

AUTH_CHANNEL = int(
    getenv(
        "AUTH_CHANNEL",
        "-1002267118144"
    )
)

FSUB = getenv(
    "FSUB",
    True
)


# ==========================================================
# LOGGER
# ==========================================================

LOGGER_GROUP_ID = -1003996256161


# ==========================================================
# AI API KEYS
# ==========================================================
#
# Heroku Config Var:
#
# API_KEY=GEMINI_KEY|GROQ_KEY|MISTRAL_KEY
#
# #1 = Gemini
# #2 = Groq
# #3 = Mistral
#
# ==========================================================

API_KEY = getenv(
    "API_KEY",
    ""
).strip()


AI_KEYS = [
    key.strip()
    for key in API_KEY.split("|")
    if key.strip()
]


# ==========================================================
# INDIVIDUAL AI KEYS
# ==========================================================

GEMINI_API_KEY = (
    AI_KEYS[0]
    if len(AI_KEYS) >= 1
    else None
)

GROQ_API_KEY = (
    AI_KEYS[1]
    if len(AI_KEYS) >= 2
    else None
)

MISTRAL_API_KEY = (
    AI_KEYS[2]
    if len(AI_KEYS) >= 3
    else None
)


# ==========================================================
# AI KEY STATUS
# ==========================================================

AI_KEY_STATUS = {
    "gemini": bool(GEMINI_API_KEY),
    "groq": bool(GROQ_API_KEY),
    "mistral": bool(MISTRAL_API_KEY),
}


# ==========================================================
# SUPPORT / CHANNELS
# ==========================================================

SUPPORT_GROUP = os.environ.get(
    "SUPPORT_GROUP",
    "ixasta1"
)

UPDATES_CHANNEL = os.environ.get(
    "UPDATES_CHANNEL",
    "ixasta1"
)


# ==========================================================
# IMAGES
# ==========================================================

IMG = [
    "https://files.catbox.moe/4q7c4w.jpg",
    "https://files.catbox.moe/90z6sq.jpg",
    "https://files.catbox.moe/rdfi4z.jpg",
    "https://files.catbox.moe/6f9rgp.jpg",
    "https://files.catbox.moe/99wj12.jpg",
    "https://files.catbox.moe/ezpnd2.jpg",
    "https://files.catbox.moe/e7q55f.jpg",
    "https://files.catbox.moe/qyfsi7.jpg",
    "https://files.catbox.moe/kbke7s.jpg",
    "https://files.catbox.moe/7icvpu.jpg",
    "https://files.catbox.moe/4hd77z.jpg",
    "https://files.catbox.moe/yn7wje.jpg",
    "https://files.catbox.moe/kifsir.jpg",
    "https://files.catbox.moe/zi21kc.jpg",
]


# ======================================================
# ©️ 2026-27 All Rights Reserved by ASTA (ASTA) 😎
#
# 🧑‍💻 Developer : t.me/zxasta
# 🔗 Source link : GitHub.com/zxasta/ASTA_CHAT
# 📢 Telegram channel : t.me/ixasta1
# =======================================================
