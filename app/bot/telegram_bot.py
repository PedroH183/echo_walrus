import logging
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
from ..ia_models.factory import AIModelFactory

class TelegramBot:
    """Telegram bot that uses AI models to respond to messages."""
    
    def __init__(self, token: str, model_type: str = 'gemini'):
        """Initialize the bot with token and AI model."""
        self.token = token

        self.logger = logging.getLogger(__name__)
        self.ai_model = AIModelFactory.create_model(model_type)
        self.application = Application.builder().token(token).build()
        self._setup_handlers()

    def _setup_handlers(self) -> None:
        """Set up command and message handlers."""
        self.application.add_handler(CommandHandler("start", self._start_command))
        self.application.add_handler(CommandHandler("help", self._help_command))
        self.application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, self._handle_message))

    async def _start_command(self, update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        """Handle /start command."""
        await update.message.reply_text('Hi! I am your AI-powered Telegram bot. Send me a message and I will respond using Gemini AI!')

    async def _help_command(self, update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        """Handle /help command."""
        await update.message.reply_text('Help! Send me any message and I will respond using Gemini AI.')

    async def _handle_message(self, update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        """Handle incoming messages."""
        try:
            response = await self.ai_model.get_response(update.message.text)
            await update.message.reply_text(response)
        except Exception as e:
            self.logger.error(f"Error processing message: {str(e)}")
            await update.message.reply_text("Sorry, I encountered an error while processing your message.")

    def run(self) -> None:
        """Start the bot."""

        try:
            self.logger.info("Starting bot...")
            self.application.add_handler(
                MessageHandler(
                    filters.TEXT & ~filters.COMMAND, self._handle_message
                )
            )
            self.application.run_polling(allowed_updates=Update.ALL_TYPES)

        except KeyboardInterrupt:
            self.logger.info("Bot stopped by user")
        except Exception as e:
            self.logger.error(f"Error running bot: {str(e)}")
            raise