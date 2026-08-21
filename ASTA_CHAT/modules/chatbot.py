import asyncio
import logging

from pyrogram import filters
from ASTA_CHAT import app
from google import genai
import config


# ==========================================================
# LOGGING
# ==========================================================

LOGGER = logging.getLogger("ASTA_CHAT_CHATBOT")


# ==========================================================
# GEMINI CLIENT
# ==========================================================

ai_client = None

API_KEY = getattr(config, "API_KEY", None)

if API_KEY:
    try:
        ai_client = genai.Client(api_key=API_KEY)
        LOGGER.info("Gemini AI client initialized successfully.")
    except Exception:
        LOGGER.exception("Failed to initialize Gemini client.")
else:
    LOGGER.error("API_KEY is missing in config.py")


# ==========================================================
# GEMINI RESPONSE
# ==========================================================

async def get_ai_response(prompt_text: str):
    if ai_client is None:
        return None

    def call_gemini():
        try:
            response = ai_client.models.generate_content(
                model="gemini-2.5-flash",
                contents=prompt_text,
            )

            if response is None:
                return None

            # New Google GenAI SDK response
            text = getattr(response, "text", None)

            if text:
                return str(text).strip()

            # Fallback response extraction
            candidates = getattr(response, "candidates", None)

            if not candidates:
                return None

            result = []

            for candidate in candidates:
                content = getattr(candidate, "content", None)

                if content is None:
                    continue

                parts = getattr(content, "parts", None)

                if not parts:
                    continue

                for part in parts:
                    part_text = getattr(part, "text", None)

                    if part_text:
                        result.append(str(part_text))

            if result:
                return "\n".join(result).strip()

            return None

        except Exception:
            LOGGER.exception("Gemini request failed.")
            return None

    return await asyncio.to_thread(call_gemini)


# ==========================================================
# CHATBOT HANDLER
# ==========================================================

@app.on_message(
    filters.text
    & ~filters.bot
    & ~filters.via_bot
)
async def chatbot_handler(client, message):

    user_prompt = message.text

    # Ignore empty messages
    if not user_prompt:
        return

    # Ignore commands
    if user_prompt.startswith("/"):
        return

    try:
        # Generate Gemini response
        reply_text = await get_ai_response(user_prompt)

        if not reply_text:
            LOGGER.warning("Gemini returned an empty response.")
            return

        # Send reply
        await message.reply_text(reply_text)

    except Exception:
        LOGGER.exception("CHATBOT FULL ERROR")
