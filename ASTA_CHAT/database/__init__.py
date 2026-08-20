# =======================================================
# ©️ 2026-27 All Rights Reserved by ASTA (ASTA) 🚀

# This source code is under MIT License 📜 Unauthorized forking, importing, or using this code without giving proper credit will result in legal action ⚠️
 
# 📩 DM for permission : @zxasta
# =======================================================

from motor.motor_asyncio import AsyncIOMotorClient
import config

ChatBot = AsyncIOMotorClient(config.MONGO_URL)
db = ChatBot["ChatBot"]  
usersdb = db["users"]    
chatsdb = db["chats"]    

chatbot_settings_db = db["chatbot_settings"]

from .chats import *
from .admin import *
from .fsub import *
from .asta import *
from .chatbot import *

# ======================================================
# ©️ 2026-27 All Rights Reserved by ASTA (ASTA) 😎

# 🧑‍💻 Developer : t.me/zxasta
# 🔗 Source link : GitHub.com/zxasta/ASTA_CHAT
# 📢 Telegram channel : t.me/ixasta1
# =======================================================
