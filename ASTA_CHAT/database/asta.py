import motor.motor_asyncio
from config import MONGO_URL

# Initialize async MongoDB client with pooling and timeout controls to prevent locks
db_client = motor.motor_asyncio.AsyncIOMotorClient(
    MONGO_URL,
    maxPoolSize=50,
    serverSelectionTimeoutMS=5000
)
db = db_client["AstaChatBot"]

async def add_served_chat(chat_id: int):
    chats = db.chats
    if not await chats.find_one({"chat_id": chat_id}):
        await chats.insert_one({"chat_id": chat_id})

async def remove_served_chat(chat_id: int):
    chats = db.chats
    await chats.delete_one({"chat_id": chat_id})

async def get_served_chats():
    chats = db.chats
    all_chats = []
    async for chat in chats.find({"chat_id": {"$exists": True}}):
        all_chats.append(chat["chat_id"])
    return all_chats
