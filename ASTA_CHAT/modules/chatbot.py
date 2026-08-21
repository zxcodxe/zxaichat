import asyncio
import logging

from pyrogram import filters
from ASTA_CHAT import app
from google import genai
import config


# ==========================================================
# LOGGING
# ==========================================================

logging.basicConfig(level=logging.INFO)
LOGGER = logging.getLogger("ASTA_CHAT_CHATBOT")


# ==========================================================
# GEMINI CLIENT
# ==========================================================

ai_client = None

if getattr(config, "API_KEY", None):
    try:
        ai_client = genai.Client(api_key=config.API_KEY)
        LOGGER.info("Gemini AI client initialized successfully.")
    except Exception as e:
        LOGGER.error(f"Failed to initialize Gemini client: {e}")
else:
    LOGGER.error("API_KEY is missing in config.py")


# ==========================================================
# GEMINI RESPONSE
# ==========================================================

async def get_ai_response(prompt_text: str):
    if not ai_client:
        return None

    def call_gemini():
        try:
            response = ai_client.models.generate_content(
                model="gemini-2.5-flash",
                contents=prompt_text,
            )

            if response is None:
                return None

            # Safely get generated text
            text = getattr(response, "text", None)

            if text:
                return str(text).strip()

            # Fallback: inspect candidates/content parts
            candidates = getattr(response, "candidates", None)

            if candidates:
                for candidate in candidates:
                    content = getattr(candidate, "content", None)

                    if not content:
                        continue

                    parts = getattr(content, "parts", None)

                    if not parts:
                        continue

                    texts = []

                    for part in parts:
                        part_text = getattr(part, "text", None)

                        if part_text:
                            texts.append(str(part_text))

                    if texts:
                        return "\n".join(texts).strip()

            return None

        except Exception as e:
            LOGGER.error(f"Gemini request error: {type(e).__name__}: {e}")
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

    # Ignore Telegram commands
    if user_prompt.startswith("/"):
        return

    try:
        # Typing indicator
        await client.send_chat_action(
            message.chat.id,
            "typing",
        )

        # Generate AI response
        reply_text = await get_ai_response(user_prompt)

        # No response from Gemini
        if not reply_text:
            return

        # Send response
        await message.reply_text(
            reply_text,
            disable_web_page_preview=True,
        )

    except Exception as e:
        LOGGER.error(
            f"Chatbot Handler Error: {type(e).__name__}: {e}"
        )
