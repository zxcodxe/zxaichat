# =======================================================
# ©️ 2026-27 All Rights Reserved by ASTA (ASTA) 🚀

# This source code is under MIT License 📜 Unauthorized forking, importing, or using this code without giving proper credit will result in legal action ⚠️
 
# 📩 DM for permission : @zxasta
# =======================================================

from typing import Callable, Union
from pyrogram.enums import ChatMemberStatus
from pyrogram.types import Message, CallbackQuery
from ASTA_CHAT import app  

def is_admins(func: Callable) -> Callable:
    async def non_admin(c: app, m: Union[Message, CallbackQuery]):
        if isinstance(m, CallbackQuery):
            admin = await c.get_chat_member(m.message.chat.id, m.from_user.id)
        else:
            admin = await c.get_chat_member(m.chat.id, m.from_user.id)
        if admin.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR]:
            return await func(c, m)

    return non_admin

# ======================================================
# ©️ 2026-27 All Rights Reserved by ASTA (ASTA) 😎

# 🧑‍💻 Developer : t.me/zxasta
# 🔗 Source link : GitHub.com/zxasta/ASTA_CHAT
# 📢 Telegram channel : t.me/ixasta1
# =======================================================
