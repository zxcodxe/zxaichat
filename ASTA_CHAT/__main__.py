# =======================================================
# ©️ 2026-27 All Rights Reserved by ASTA (ASTA) 🚀

# This source code is under MIT License 📜 Unauthorized forking, importing, or using this code without giving proper credit will result in legal action ⚠️
 
# 📩 DM for permission : @zxasta
# =======================================================

import importlib

from pyrogram import idle

from ASTA_CHAT import app
from ASTA_CHAT.modules import ALL_MODULES


async def boot():
    for module in ALL_MODULES:
        importlib.import_module(f"ASTA_CHAT.modules.{module}")

    await app.start()

    await idle()

    await app.stop()


if __name__ == "__main__":
    app.run(boot())


# ======================================================
# ©️ 2026-27 All Rights Reserved by ASTA (ASTA) 😎

# 🧑‍💻 Developer : t.me/zxasta
# 🔗 Source link : GitHub.com/zxasta/ASTA_CHAT
# 📢 Telegram channel : t.me/ixasta1
# =======================================================
