# =======================================================
# ©️ 2026-27 All Rights Reserved by ASTA (ASTA) 🚀
# =======================================================

import logging
from pyrogram import filters
from ASTA_CHAT import app
from ASTA_CHAT.database.asta import fetch_asta, ASTA_CHAT_api

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


@app.on_message(filters.text & ~filters.private)
async def chatbot_reply(_, message):
    if not message.text:
        return

    user_message = message.text.strip()
    chat_id = message.chat.id
    user_id = message.from_user.id if message.from_user else 0

    try:
        # Step 1: Check Database first
        reply = await fetch_asta(user_message)

        # Step 2: If not in DB, use Sunena AI (ChatGptEs)
        if not reply:
            reply = await ASTA_CHAT_api.ask_question(
                message=user_message,
                chat_id=chat_id,
                user_id=user_id
            )

        if reply:
            await message.reply_text(reply)

    except Exception as e:
        logger.error(f"Chatbot Module Error: {e}", exc_info=True)
        await message.reply_text("Sorry, abhi answer generate nahi ho paaya 😅 ek baar phir bhejo.")
