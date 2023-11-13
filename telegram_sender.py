from telegram import Bot

class TelegramSender:
    def __init__(self, token):
        self.bot = Bot(token)

    async def send_message(self, chat_id, message):
        try:
            await self.bot.send_message(chat_id=chat_id, text=message)
            print("Message sent successfully!")
        except Exception as e:
            print(f"Error sending message: {e}")


# Usage Example

if __name__ == "__main__":
    import asyncio

     
    bot_token = 'YOUR_TOKEN'
    chat_id = 'chat ID' 

    async def main():
        sender = TelegramSender(bot_token)
        await sender.send_message(chat_id, "This Message Sent by Python")

    
    asyncio.run(main())
