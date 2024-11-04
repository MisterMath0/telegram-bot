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


