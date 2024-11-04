# Telegram Translation Bot

A Telegram bot that translates messages from French to English using OpenAI's GPT model. The bot preserves the formatting of messages, improves readability, and reformats prices (e.g., converts `66 000 USD` to `66,000USD`).

## Features

- Translates messages from French to English.
- Automatically formats prices to improve readability.
- Sends empty text if the message is already in English.

## Prerequisites

- Python 3.8 or higher
- [OpenAI API key](https://beta.openai.com/signup/)
- [Telegram bot token](https://core.telegram.org/bots#3-how-do-i-create-a-bot) (using [BotFather](https://core.telegram.org/bots#botfather) to create your bot)

## Setup

### Step 1: Clone the Repository

1. Clone this repository:
   ```bash
   git clone https://github.com/MisterMath0/telegram-bot.git
   cd telegram-bot
2. Install Dependencies
   ```bash
   pip install python-telegram-bot openai python-dotenv
3. Set Up Environment Variables
   1. Create a .env file to securely store sensitive information:
   ```bash
   touch .env
   ```
   2. Open the .env file in a text editor and add your OpenAI and Telegram bot API keys:
      ```bash
      OPENAI_API_KEY="your_openai_api_key"
      TELEGRAM_BOT_TOKEN="your_telegram_bot_token"
4. Modify bot.py to Load Environment Variables
Add the following lines to bot.py to load environment variables:
   ```bash
   import os
   from dotenv import load_dotenv

   load_dotenv()

   openai.api_key = os.getenv("OPENAI_API_KEY")
   token = os.getenv("TELEGRAM_BOT_TOKEN")

## Usage
- Start the bot: Send the /start command in Telegram to initialize communication.
- Translate a message: Send a message in French, and the bot will respond with the English translation. If the message is already in English, the bot will return an empty response.
- Format prices: The bot will automatically reformat prices (e.g., 66 000 USD to 66,000USD).

## Troubleshooting
Common Errors
- Message text is empty: Ensure that the bot receives text input. Non-text messages (images, stickers, etc.) are ignored by the bot.
- Invalid API keys: Verify that your OpenAI and Telegram bot tokens are correctly stored in the .env file.
## Log Files
Logging is set up to output to the console. You can redirect logs to a file by modifying the logging.basicConfig line in bot.py.







