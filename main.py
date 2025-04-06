import os
import logging

from app.bot.telegram_bot import TelegramBot
import asyncio

def main():
    """Main function to run the bot."""

    logging.basicConfig(
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        level=logging.INFO
    )

    token = os.getenv('TELEGRAM_BOT_TOKEN')
    if not token:
        raise ValueError("No token provided. Set the TELEGRAM_BOT_TOKEN environment variable.")

    # Create and run the bot
    bot = TelegramBot(token)
    bot.run()

if __name__ == "__main__":
   main()