import asyncio
from pyrogram import filters
from ASTA_CHAT import app
from google import genai
import config

# Naye SDK ke saath client setup
ai_client = None
if config.API_KEY:
    ai_client = genai.Client(api_key=config.API_KEY)

async def get_ai_response(prompt_text):
    def call_gemini():
        # Naye SDK ka official syntax: client.models.generate_content
        response = ai_client.models.generate_content(
            model='gemini-2.5-flash',  # ya 'gemini-1.5-flash'
            contents=prompt_text,
        )
        return response.text
    return await asyncio.to_thread(call_gemini)

@app.on_message(filters.text & ~filters.bot & ~filters.via_bot)
async def chatbot_handler(client, message):
    user_prompt = message.text
    
    # Commands aur empty messages ko ignore karo
    if not user_prompt or user_prompt.startswith("/"):
        return

    try:
        await client.send_chat_action(message.chat.id, "typing")
        
        reply_text = await get_ai_response(user_prompt)
        
        if reply_text:
            await message.reply_text(reply_text)
            
    except Exception as e:
        print(f"Chatbot Error: {e}")
