# =======================================================
# ©️ 2026-27 All Rights Reserved by ASTA (ASTA) 🚀
# =======================================================

from pyrogram import filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.enums import ChatAction

from ASTA_CHAT import app
from ASTA_CHAT.database import (
    is_ASTA_CHAT_enabled,
    enable_ASTA_CHAT,
    disable_ASTA_CHAT,
    ASTA_CHAT_api,
    is_admins,
)


# Every normal text message in an enabled group is eligible.
# Mentions are NOT required; tagging the bot also works naturally.
def valid_group_message(_, __, message: Message):
    if not message.text:
        return False
    text = message.text.strip()
    if not text or text.startswith(("/", "!")):
        return False
    return len(text) <= 4000


GROUP_CHAT_FILTER = filters.create(valid_group_message)


@app.on_message(
    filters.group
    & GROUP_CHAT_FILTER
    & ~filters.bot
    & ~filters.sticker
)
async def ASTA_CHAT_group(_, message: Message):
    chat_id = message.chat.id

    if not await is_ASTA_CHAT_enabled(chat_id):
        return

    user_id = message.from_user.id if message.from_user else 0

    await app.send_chat_action(chat_id, ChatAction.TYPING)
    reply = await ASTA_CHAT_api.ask_question(
        message.text,
        chat_id=chat_id,
        user_id=user_id,
    )

    if reply:
        await message.reply_text(reply)


@app.on_message(
    filters.private
    & filters.text
    & ~filters.bot
    & ~filters.regex(r"^[/!]")
)
async def ASTA_CHAT_pm(_, message: Message):
    user_id = message.from_user.id if message.from_user else 0

    await app.send_chat_action(message.chat.id, ChatAction.TYPING)
    reply = await ASTA_CHAT_api.ask_question(
        message.text,
        chat_id=message.chat.id,
        user_id=user_id,
    )

    if reply:
        await message.reply_text(reply)


@app.on_message(filters.command("chatbot") & filters.group & ~filters.bot)
@is_admins
async def ASTA_CHAT_toggle(_, message: Message):
    chat_id = message.chat.id
    chat_title = message.chat.title

    status = await is_ASTA_CHAT_enabled(chat_id)
    status_text = "ᴇɴᴀʙʟᴇᴅ" if status else "ᴅɪꜱᴀʙʟᴇᴅ"

    keyboard = InlineKeyboardMarkup(
        [[
            InlineKeyboardButton("ᴇɴᴀʙʟᴇ", callback_data="ASTA_CHAT_enable"),
            InlineKeyboardButton("ᴅɪꜱᴀʙʟᴇ", callback_data="ASTA_CHAT_disable")
        ]]
    )

    await message.reply_text(
        f"❖ ᴄᴜʀʀᴇɴᴛʟʏ ᴄʜᴀᴛʙᴏᴛ ɪꜱ **{status_text}** ɪɴ **{chat_title}**.",
        reply_markup=keyboard
    )


@app.on_callback_query(filters.regex(r"^ASTA_CHAT_(enable|disable)$"))
@is_admins
async def ASTA_CHAT_button_toggle(_, query):
    chat_id = query.message.chat.id
    user = query.from_user

    if query.data == "ASTA_CHAT_enable":
        if await is_ASTA_CHAT_enabled(chat_id):
            await query.answer("ᴄʜᴀᴛʙᴏᴛ ɪꜱ ᴀʟʀᴇᴀᴅʏ ᴇɴᴀʙʟᴇᴅ.", show_alert=True)
            return
        await enable_ASTA_CHAT(chat_id)
        await query.message.edit_text(
            f"❖ ᴄʜᴀᴛʙᴏᴛ ʜᴀꜱ ʙᴇᴇɴ **ᴇɴᴀʙʟᴇᴅ** ʙʏ {user.mention}."
        )
        await query.answer("ᴄʜᴀᴛʙᴏᴛ ᴇɴᴀʙʟᴇᴅ !!")

    else:
        if not await is_ASTA_CHAT_enabled(chat_id):
            await query.answer("ᴄʜᴀᴛʙᴏᴛ ɪꜱ ᴀʟʀᴇᴀᴅʏ ᴅɪꜱᴀʙʟᴇᴅ.", show_alert=True)
            return
        await disable_ASTA_CHAT(chat_id)
        await query.message.edit_text(
            f"❖ ᴄʜᴀᴛʙᴏᴛ ʜᴀꜱ ʙᴇᴇɴ **ᴅɪꜱᴀʙʟᴇᴅ** ʙʏ {user.mention}."
        )
        await query.answer("ᴄʜᴀᴛʙᴏᴛ ᴅɪꜱᴀʙʟᴇᴅ !!")

# ======================================================
# ©️ 2026-27 All Rights Reserved by ASTA (ASTA) 😎
# =======================================================
