# =======================================================
# ©️ 2026-27 All Rights Reserved by ASTA (ASTA) 🚀

# This source code is under MIT License 📜 Unauthorized forking, importing, or using this code without giving proper credit will result in legal action ⚠️
 
# 📩 DM for permission : @zxasta
# =======================================================

import time
import logging

from pyrogram import Client
from motor.motor_asyncio import AsyncIOMotorClient

import config

logging.basicConfig(
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt="%d-%b-%y %H:%M:%S",
    level=logging.INFO,
)
LOGGER = logging.getLogger("ASTA_CHAT")

db = AsyncIOMotorClient(config.MONGO_URL).ASTA
START_TIME = time.time()


class Bot(Client):
    def __init__(self):
        super().__init__(
            name="ASTA_CHAT",
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            bot_token=config.BOT_TOKEN,
        )

    async def start(self, *args, **kwargs):    
        await super().start()
        self.id = self.me.id
        self.name = self.me.first_name
        self.username = self.me.username
        LOGGER.info(f"Bot started as {self.name} (@{self.username}). 💫")

    async def stop(self):
        await super().stop()
        LOGGER.info("Bot stopped. 😔")

app = Bot()

# ======================================================
# ©️ 2026-27 All Rights Reserved by ASTA (ASTA) 😎

# 🧑‍💻 Developer : t.me/zxasta
# 🔗 Source link : GitHub.com/zxasta/ASTA_CHAT
# 📢 Telegram channel : t.me/ixasta1
# =======================================================
