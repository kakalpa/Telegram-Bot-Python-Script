import asyncio
from telegram import Bot

async def get_chat_id(bot_token):
    bot = Bot(bot_token)
    updates = await bot.get_updates()

    if updates:
        chat_id = updates[0].message.chat_id
        print(f"Your chat ID is: {chat_id}")
    else:
        print("No updates received. Send a message to your bot first.")

if __name__ == "__main__":
    
    bot_token = 'YOUR_TOKEN' # Replace this

  
    asyncio.run(get_chat_id(bot_token))
