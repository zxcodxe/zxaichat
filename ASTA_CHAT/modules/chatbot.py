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
        LOGGER.error("Gemini client is not initialized.")
        return None

    # Make sure prompt is actually valid
    if not isinstance(prompt_text, str):
        return None

    prompt_text = prompt_text.strip()

    if not prompt_text:
        LOGGER.warning("Empty prompt received. Skipping Gemini request.")
        return None

    def call_gemini():

        try:
            response = ai_client.models.generate_content(
                model="gemini-3.6-flash",
                contents=prompt_text,
            )

            if response is None:
                return None

            text = getattr(response, "text", None)

            if text:
                text = str(text).strip()

                if text:
                    return text

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
                        part_text = str(part_text).strip()

                        if part_text:
                            result.append(part_text)

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

    try:

        # Get message text safely
        user_prompt = message.text

        # Ignore missing text
        if not isinstance(user_prompt, str):
            return

        # Remove unnecessary spaces
        user_prompt = user_prompt.strip()

        # Ignore empty messages
        if not user_prompt:
            return

        # Ignore Telegram commands
        if user_prompt.startswith("/"):
            return

        # Generate AI response
        reply_text = await get_ai_response(user_prompt)

        # No response
        if not reply_text:
            LOGGER.warning(
                "Gemini returned an empty response."
            )
            return

        # Send response
        await message.reply_text(reply_text)

    except Exception:
        LOGGER.exception("CHATBOT FULL ERROR")
