import asyncio
from pyrogram import filters
from ASTA_CHAT import app
import google.generativeai as genai
import config

# Configure Gemini API safely
if config.API_KEY:
    genai.configure(api_key=config.API_KEY)

async def get_ai_response(prompt_text):
    def call_gemini():
        model = genai.GenerativeModel('gemini-1.5-flash')
        response = model.generate_content(prompt_text)
        return response.text
    return await asyncio.to_thread(call_gemini)

@app.on_message(filters.text & ~filters.bot & ~filters.via_bot)
async def chatbot_handler(client, message):
    user_prompt = message.text
    
    # Ignore commands or empty inputs
    if not user_prompt or user_prompt.startswith("/"):
        return

    try:
        # Prevent event loop blockage by running typing action asynchronously
        await client.send_chat_action(message.chat.id, "typing")
        
        reply_text = await get_ai_response(user_prompt)
        
        if reply_text:
            await message.reply_text(reply_text)
            
    except Exception as e:
        print(f"Chatbot Error: {e}")
        # Fail silently or log to avoid flooding chat with error notes during high traffic
