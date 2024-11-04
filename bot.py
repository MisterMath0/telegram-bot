import openai
import logging
import re
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters

# Set up logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

# OpenAI API Key - Replace with your actual OpenAI API Key securely
openai.api_key = 'YOUR_OPENAI_API_KEY'

# System message for ChatGPT
system_message = ("You're a helpful telegram bot assistant. Your role is to translate messages, format messages, "
                  "and output them from French to English (if the language is already in English, send an empty text) "
                  "without anything else. Keep the same format in markup and add a line space between each line to ensure "
                  "they are well readable and visible. Also, make sure that prices are written correctly without spaces between "
                  "them, only use commas (e.g., change 66 000 USD to 66,000USD).")

# Function to check and format prices
def format_prices(text):
    # Regex to match prices like '66 000 USD' and change it to '66,000USD'
    return re.sub(r'(\d{1,3})(?: \d{3})+( USD)', lambda m: f"{m.group(1)}{m.group(0).replace(' ', ',')}", text)

# OpenAI API call function
async def translate_message(message):
    try:
        response = await openai.ChatCompletion.acreate(
            model="gpt-4",
            messages=[{"role": "system", "content": system_message},
                      {"role": "user", "content": message}]
        )
        translated_message = response.choices[0].message['content']
        return format_prices(translated_message)
    except Exception as e:
        logger.error(f"Error in translate_message: {e}")
        return ""

# Message handler for incoming messages
async def handle_message(update: Update, context):
    try:
        # Check if the message is a text message
        if update.message and update.message.text:
            user_message = update.message.text
            logger.info(f"Received message: {user_message}")

            # Translate and process the message
            translated_message = await translate_message(user_message)

            # Send the translated message if it's not empty
            if translated_message.strip():
                await update.message.reply_text(translated_message)
            else:
                logger.info("Translated message is empty; sending an empty text.")
                await update.message.reply_text("")  # Send an empty text if the message is in English
        else:
            logger.warning("Received a non-text message or update without a message.")

    except Exception as e:
        logger.error(f"Error handling message: {e}")
        await update.message.reply_text("An error occurred while processing your message.")

# Start command handler
async def start(update: Update, context):
    await update.message.reply_text("Hello! I am a bot that translates messages from French to English and formats them. Send me a message to try!")

# Main function to set up the bot
async def main():
    # Replace with your Telegram bot token
    token = 'YOUR_TELEGRAM_BOT_TOKEN'
    application = ApplicationBuilder().token(token).build()

    # Add command and message handlers
    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    # Start the bot
    await application.run_polling()

if __name__ == '__main__':
    import asyncio
    asyncio.run(main())
