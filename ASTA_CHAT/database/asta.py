# =======================================================
# ©️ 2026-27 All Rights Reserved by ASTA (ASTA) 🚀
# =======================================================

import asyncio
import logging
from collections import defaultdict, deque
from google import genai
from google.genai import types
from motor.motor_asyncio import AsyncIOMotorClient

# Flexible import to handle both MONGO_DB_URI and MONGO_URL
try:
    from config import API_KEY, MONGO_DB_URI
except ImportError:
    from config import API_KEY, MONGO_URL as MONGO_DB_URI

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Initialize MongoDB Connection
try:
    if MONGO_DB_URI:
        mongo_client = AsyncIOMotorClient(MONGO_DB_URI)
        db = mongo_client["ASTA_DB"]
        astadb = db["asta_collection"]
    else:
        logger.warning("MongoDB URI not provided in config.")
        astadb = None
except Exception as e:
    logger.error(f"MongoDB Init Error: {e}")
    astadb = None


async def fetch_asta(word: str):
    if astadb is None:
        return None
    try:
        word = word.lower().strip()
        x = await astadb.find_one({"word": word})
        if x:
            return x.get("text")
    except Exception as e:
        logger.error(f"Database Fetch Error: {e}")
    return None


class ChatGptEs:
    SYSTEM_PROMPT = r"""
You are Sunena, a friendly, sweet and caring AI chat assistant used in Telegram.

PERSONALITY:
- Be warm, natural, playful and respectful.
- Sound like a friendly girl, but never claim to be a real human.
- Match the user's tone: casual when they are casual, serious when they are serious.
- Use emojis naturally.

LANGUAGE:
- Automatically detect the language and writing style of the user's latest message.
- Reply in the same language and script whenever possible.
- Roman Hindi/Hinglish -> Roman Hindi/Hinglish.
- English -> English.

STYLE:
- Casual chat: usually 1-3 short sentences.
"""

    def __init__(self, api_key: str):
        if not api_key:
            raise ValueError("API_KEY is missing")
        self.client = genai.Client(api_key=api_key)
        # Primary model and automatic fallbacks if 503 Server Busy occurs
        self.models = ["gemini-2.5-flash", "gemini-2.0-flash", "gemini-1.5-flash"]
        self.history = defaultdict(lambda: deque(maxlen=8))

    def _build_prompt(self, key, message: str) -> str:
        history = self.history[key]
        context = "\n".join(f"{role}: {text}" for role, text in history)
        if context:
            context = f"\nRECENT CONVERSATION:\n{context}\n"
        return (
            f"{self.SYSTEM_PROMPT}\n"
            f"{context}\n"
            f"LATEST USER MESSAGE:\n{message}\n\n"
            "Reply naturally to the latest user message."
        )

    async def ask_question(self, message: str, chat_id: int = 0, user_id: int = 0) -> str:
        key = (chat_id, user_id)
        prompt = self._build_prompt(key, message)
        
        config = types.GenerateContentConfig(
            temperature=0.7,
            automatic_function_calling=types.AutomaticFunctionCallingConfig(disable=True)
        )

        # Loop through fallback models if primary model returns 503 High Demand
        for model_name in self.models:
            try:
                response = await self.client.aio.models.generate_content(
                    model=model_name,
                    contents=prompt,
                    config=config
                )
                
                text = (response.text or "").strip()
                if text:
                    self.history[key].append(("User", message))
                    self.history[key].append(("Sunena", text))
                    return text
            except Exception as e:
                logger.warning(f"Model {model_name} failed ({e}). Switching to next fallback model...")
                await asyncio.sleep(0.1)

        return "Sorry, abhi traffic jyada hai, thodi der baad try karo 😅"


ASTA_CHAT_api = ChatGptEs(api_key=API_KEY)
