# Echo Walrus - Smart Telegram Bot

This is a Telegram bot that can talk with you using AI (Artificial Intelligence). It uses Gemini AI to understand and answer your messages.

## What This Bot Can Do

- 🤖 Talks with you using AI
- 💬 Has simple commands like /start and /help
- 🔄 Answers your messages quickly
- 🛡️ Handles errors well
- 🔌 Easy to add new AI features

## What You Need

- Python 3.13 or newer
- A Telegram Bot Token (get it from @BotFather)
- A Gemini API Key
- Docker and Docker Compose (if you want to use containers)

## How to Install

1. Get the code:
```bash
git clone https://github.com/yourusername/echo-walrus.git
cd echo-walrus
```

2. Set up your keys:
```bash
cp .env.example .env
```
Open the `.env` file and add your keys:
```
TELEGRAM_BOT_TOKEN=your_telegram_bot_token
GEMINI_API_KEY=your_gemini_api_key
```

3. Start the bot:
```bash
docker compose up -d
```

## How to Use

After starting, the bot will be ready to talk with you. Send `/start` to begin.

## Bot Commands

- `/start` - Start talking with the bot
- `/help` - Get help information

## Files in This Project

```
echo_walrus/
├── app/
│   ├── bot/
│   │   └── telegram_bot.py
│   └── ia_models/
│       ├── base.py
│       ├── gemini.py
│       └── factory.py
├── main.py
├── setup.py
├── docker-compose.yml
├── Dockerfile
└── README.md
```

## License

This project uses the MIT License. You can use it for free.
