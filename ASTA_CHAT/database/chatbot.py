# =======================================================
# ©️ 2026-27 All Rights Reserved by ASTA (ASTA) 🚀
#
# This source code is under MIT License 📜
# 📩 DM for permission : @zxasta
# =======================================================

from . import chatbot_settings_db, chatsdb, usersdb


# =======================================================
# CHATBOT ENABLE / DISABLE
# =======================================================

async def is_ASTA_CHAT_enabled(chat_id: int) -> bool:
    """
    Returns True when AI chatbot is enabled for the chat.
    """

    chat = await chatbot_settings_db.find_one(
        {"chat_id": chat_id}
    )

    return chat is None


async def enable_ASTA_CHAT(chat_id: int):
    """
    Enable AI chatbot for a chat.
    """

    await chatbot_settings_db.delete_one(
        {"chat_id": chat_id}
    )


async def disable_ASTA_CHAT(chat_id: int):
    """
    Disable AI chatbot for a chat.
    """

    if not await chatbot_settings_db.find_one(
        {"chat_id": chat_id}
    ):
        await chatbot_settings_db.insert_one(
            {"chat_id": chat_id}
        )


async def get_enabled_chats() -> list:
    """
    Return all chats where AI chatbot is enabled.
    """

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


async def set_user_language(
    user_id: int,
    language: str,
) -> bool:
    """
    Save user's selected language.

    Example:
        set_user_language(123456789, "hi")
    """

    language = str(language).lower().strip()

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


async def get_user_language(
    user_id: int,
) -> str:
    """
    Get user's saved language.

    English is used as the default language.
    """

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

    return "en"


async def reset_user_language(
    user_id: int,
) -> bool:
    """
    Reset user's language back to English.
    """

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
    """
    Convert language code into readable name.
    """

    return SUPPORTED_LANGUAGES.get(
        str(language).lower(),
        "English",
    )


# =======================================================
# LANGUAGE CHECK
# =======================================================

def is_supported_language(
    language: str,
) -> bool:
    """
    Check whether a language is supported.
    """

    return (
        str(language).lower().strip()
        in SUPPORTED_LANGUAGES
    )


# =======================================================
# ©️ 2026-27 ASTA
# Developer : @zxasta
# Support   : @ixasta1
# =======================================================
