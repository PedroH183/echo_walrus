# Echo Walrus Telegram Bot

This is a simple Telegram bot that echo back messages what you send to it. The bot is build with Python and use the python-telegram-bot library.

## Features

- Echo back messages
- Simple commands like /start and /help
- Easy to use and setup

## How to Install

1. First, you need to have Docker install on your computer
2. Clone this repository to your local machine
3. Build the Docker image:
   ```bash
   docker build -t echo-walrus .
   ```
4. Create a new bot on Telegram using BotFather and get your token
5. Run the bot with your token:
   ```bash
   docker run -e TELEGRAM_BOT_TOKEN='your-token-here' echo-walrus
   ```

## How to Use

1. The bot will start automatically when you run the Docker container
2. Open Telegram and search for your bot
3. Send any message and the bot will repeat it back to you
4. Use /start to begin and /help to see help information

## Requirements

- Docker installed on your system
- A Telegram account
- A bot token from BotFather

## License

This project is under MIT License. You can use it for free for any purpose.
