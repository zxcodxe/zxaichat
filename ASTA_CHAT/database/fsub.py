# =======================================================
# ©️ 2026-27 All Rights Reserved by ASTA (ASTA) 🚀
#
# This source code is under MIT License 📜
#
# 📩 DM for permission : @zxasta
# =======================================================

import random

from pyrogram.errors import (
    UserNotParticipant,
    ChannelInvalid,
    ChatAdminRequired,
)
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from config import AUTH_CHANNEL, IMG


async def get_fsub(bot, message):
    user_id = message.from_user.id
    target_channel_id = AUTH_CHANNEL

    try:
        # Check whether the user has joined the FSub channel
        member = await bot.get_chat_member(
            target_channel_id,
            user_id,
        )

        # These statuses mean the user is not a normal member
        if member.status in ("kicked", "left"):
            raise UserNotParticipant

        return True

    except UserNotParticipant:
        try:
            chat = await bot.get_chat(target_channel_id)

            # Get a usable invite/username link
            channel_link = chat.invite_link

            if not channel_link:
                if chat.username:
                    channel_link = f"https://t.me/{chat.username}"
                else:
                    return False

            join_button = InlineKeyboardButton(
                "ᴊᴏɪɴ ᴄʜᴀɴɴᴇʟ",
                url=channel_link,
            )

            keyboard = [[join_button]]

            await message.reply_photo(
                photo=random.choice(IMG),
                caption=(
                    f"**❖ ʜᴇʏ {message.from_user.mention} "
                    f"ᴡʜᴀᴛ ᴀʀᴇ ʏᴏᴜ ᴅᴏɪɴɢ? 🤔**\n\n"
                    f"**» ᴘʟᴇᴀsᴇ ᴊᴏɪɴ ᴍʏ ᴜᴘᴅᴀᴛᴇ "
                    f"[ᴄʜᴀɴɴᴇʟ]({channel_link}) ᴛʜᴇɴ "
                    f"sᴇɴᴅ /start ᴀɢᴀɪɴ ғᴏʀ sᴇᴇ ᴍʏ "
                    f"ᴄᴏᴍᴍᴀɴᴅ ᴍᴇɴᴜ 📋**"
                ),
                reply_markup=InlineKeyboardMarkup(keyboard),
            )

            return False

        except (ChannelInvalid, ChatAdminRequired):
            # FSub channel cannot be accessed by the bot.
            # Do not crash the complete bot.
            return False

        except Exception:
            return False

    except (ChannelInvalid, ChatAdminRequired):
        # Channel ID/access problem should not crash the bot.
        return False

    except Exception:
        # Keep FSub failures from crashing the bot.
        return False


# ======================================================
# ©️ 2026-27 All Rights Reserved by ASTA (ASTA) 😎
#
# 🧑‍💻 Developer : t.me/zxasta
# 🔗 Source link : GitHub.com/zxasta/ASTA_CHAT
# 📢 Telegram channel : t.me/ixasta1
# =======================================================
