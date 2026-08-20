# =======================================================
# ©️ 2026-27 All Rights Reserved by ASTA (ASTA) 🚀
# =======================================================

import logging
import os
from pyrogram import filters
from ASTA_CHAT import app
from ASTA_CHAT.database.asta import fetch_asta
from google import genai

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Environment variable se API key fetch karna
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

# Gemini Client setup
client = genai.Client(api_key=GEMINI_API_KEY) if GEMINI_API_KEY else None


@app.on_message(filters.text & ~filters.private)
async def chatbot_reply(_, message):
    if not message.text:
        return

    user_message = message.text.strip()

    try:
        # 1. Pehle Database me check karo
        reply = await fetch_asta(user_message)

        # 2. Agar DB me jawab na ho, toh Async Gemini API Call karein
        if not reply:
            if not client:
                logger.error("GEMINI_API_KEY missing in environment variables!")
                await message.reply_text("API key setup nahi hai! Environment variable check karein.")
                return

            # Fixing Async Call using client.aio and valid model name
            response = await client.aio.models.generate_content(
                model="gemini-2.5-flash",
                contents=user_message
            )

            if response and response.text:
                reply = response.text

        # Reply send karein
        if reply:
            await message.reply_text(reply)

    except Exception as e:
        logger.error(f"Chatbot Error Details: {e}", exc_info=True)
        await message.reply_text("Sorry, abhi answer generate nahi ho paaya 😅 ek baar phir bhejo.")

# ======================================================
# ©️ 2026-27 All Rights Reserved by ASTA (ASTA) 😎
# =======================================================
