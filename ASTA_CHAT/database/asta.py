# =======================================================
# ©️ 2026-27 All Rights Reserved by ASTA (ASTA) 🚀
# =======================================================

import asyncio
import logging
from collections import defaultdict, deque
from google import genai
from google.genai import types
from motor.motor_asyncio import AsyncIOMotorClient

# Flexible import to prevent MONGO_DB_URI / MONGO_URL import crashes
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
        logger.warning("MongoDB URI missing in config file.")
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
    SYSTEM_PROMPT = r"""You are Sunena, a friendly, sweet Telegram AI assistant.
- Be warm, playful, sweet and natural.
- Reply in the same language/script as the user (Roman Hindi/Hinglish/English).
- Keep replies VERY SHORT (1-2 short sentences max)."""

    def __init__(self, api_key: str):
        if not api_key:
            raise ValueError("API_KEY is missing")
        self.client = genai.Client(api_key=api_key)
        # Active Gemini 2026 Models
        self.models = ["gemini-3.6-flash", "gemini-3.5-flash", "gemini-1.5-flash-8b"]
        # History deque reduced to maxlen=4 for maximum response speed
        self.history = defaultdict(lambda: deque(maxlen=4))

    def _build_prompt(self, key, message: str) -> str:
        history = self.history[key]
        context = "\n".join(f"{role}: {text}" for role, text in history)
        if context:
            return f"{self.SYSTEM_PROMPT}\n\nHistory:\n{context}\nUser: {message}"
        return f"{self.SYSTEM_PROMPT}\n\nUser: {message}"

    async def ask_question(self, message: str, chat_id: int = 0, user_id: int = 0) -> str:
        key = (chat_id, user_id)
        prompt = self._build_prompt(key, message)
        
        # Token cap & AFC disable for instant generation speed
        config = types.GenerateContentConfig(
            temperature=0.6,
            max_output_tokens=100,
            automatic_function_calling=types.AutomaticFunctionCallingConfig(disable=True)
        )

        for model_name in self.models:
            try:
                # Native non-blocking Async call
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
                logger.warning(f"Model {model_name} skipped: {e}")

        return "Sorry, abhi response delay ho raha hai 😅"


ASTA_CHAT_api = ChatGptEs(api_key=API_KEY)
