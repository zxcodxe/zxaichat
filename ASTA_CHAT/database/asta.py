import asyncio
from pyrogram import filters
from ASTA_CHAT import app
import google.generativeai as genai

# Async execution helper
async def get_ai_response(prompt_text):
    return await asyncio.to_thread(sync_gemini_call, prompt_text)

def sync_gemini_call(prompt_text):
    model = genai.GenerativeModel('gemini-1.5-flash')
    response = model.generate_content(prompt_text)
    return response.text

@app.on_message(filters.text & ~filters.bot)
async def chatbot_handler(client, message):
    # Sirf naya message text uthao, unwanted context hata do
    user_prompt = message.text

    if not user_prompt:
        return

    try:
        # Action status (typing)
        await client.send_chat_action(message.chat.id, "typing")
        
        # Async response generation
        reply_text = await get_ai_response(user_prompt)
        
        await message.reply_text(reply_text)
    except Exception as e:
        print(f"Chatbot Error: {e}")
        await message.reply_text("Abhi response dene mein issue aa raha hai, please thodi der baad try karein.")
