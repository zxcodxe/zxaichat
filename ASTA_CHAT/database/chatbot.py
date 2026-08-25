# =======================================================
# ©️ 2026-27 All Rights Reserved by ASTA (ASTA) 🚀
#
# This source code is under MIT License 📜
# Unauthorized forking, importing, or using this code
# without giving proper credit will result in legal action ⚠️
#
# 📩 DM for permission : @zxasta
# =======================================================

from . import chatbot_settings_db, chatsdb, usersdb


# =======================================================
# ASTA CHAT ENABLE / DISABLE
# =======================================================

async def is_ASTA_CHAT_enabled(chat_id: int) -> bool:
    chat = await chatbot_settings_db.find_one(
        {"chat_id": chat_id}
    )

    return chat is None


async def enable_ASTA_CHAT(chat_id: int):
    await chatbot_settings_db.delete_one(
        {"chat_id": chat_id}
    )


async def disable_ASTA_CHAT(chat_id: int):
    if not await chatbot_settings_db.find_one(
        {"chat_id": chat_id}
    ):
        await chatbot_settings_db.insert_one(
            {"chat_id": chat_id}
        )


async def get_enabled_chats() -> list:
    disabled = await chatbot_settings_db.find(
        {},
        {
            "chat_id": 1,
            "_id": 0,
        },
    ).to_list(length=None)

    disabled_ids = {
        item["chat_id"]
        for item in disabled
        if "chat_id" in item
    }

    all_chats = await chatsdb.find(
        {},
        {
            "chat_id": 1,
            "_id": 0,
        },
    ).to_list(length=None)

    return [
        chat["chat_id"]
        for chat in all_chats
        if chat.get("chat_id") not in disabled_ids
    ]


# =======================================================
# USER LANGUAGE SYSTEM
# =======================================================

SUPPORTED_LANGUAGES = {
    "en": "English",
    "hi": "Hindi",
    "ur": "Urdu",
    "ar": "Arabic",
    "bn": "Bengali",
    "ta": "Tamil",
}


# =======================================================
# SET USER LANGUAGE
# =======================================================

async def set_user_language(
    user_id: int,
    language: str,
) -> bool:

    language = str(
        language
    ).lower().strip()

    if language not in SUPPORTED_LANGUAGES:
        return False

    await usersdb.update_one(
        {"user_id": user_id},
        {
            "$set": {
                "language": language,
            }
        },
        upsert=True,
    )

    return True


# =======================================================
# GET USER LANGUAGE
# =======================================================

async def get_user_language(
    user_id: int,
) -> str:

    user = await usersdb.find_one(
        {"user_id": user_id},
        {
            "language": 1,
            "_id": 0,
        },
    )

    if user and user.get("language"):

        language = str(
            user["language"]
        ).lower().strip()

        if language in SUPPORTED_LANGUAGES:
            return language

    # Default language
    return "en"


# =======================================================
# RESET USER LANGUAGE
# =======================================================

async def reset_user_language(
    user_id: int,
) -> bool:

    result = await usersdb.update_one(
        {"user_id": user_id},
        {
            "$set": {
                "language": "en",
            }
        },
        upsert=True,
    )

    return result.acknowledged


# =======================================================
# LANGUAGE NAME
# =======================================================

def get_language_name(
    language: str,
) -> str:

    return SUPPORTED_LANGUAGES.get(
        str(language).lower().strip(),
        "English",
    )


# =======================================================
# CHECK SUPPORTED LANGUAGE
# =======================================================

def is_supported_language(
    language: str,
) -> bool:

    return (
        str(language).lower().strip()
        in SUPPORTED_LANGUAGES
    )


# ======================================================
# ©️ 2026-27 All Rights Reserved by ASTA (ASTA) 😎
#
# 🧑‍💻 Developer : t.me/zxasta
# 🔗 Source link : GitHub.com/zxasta/ASTA_CHAT
# 📢 Telegram channel : t.me/ixasta1
# =======================================================
