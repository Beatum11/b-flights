# Flight-Price-Tracker Bot

## Overview
The Flight-Price-Tracker bot is a Telegram bot designed to help users find the lowest price for a specific flight over the next six months. By utilizing the Aviasales API, the bot continuously monitors flight prices and notifies users when a lower price is found. The bot also features a comprehensive list of IATA codes for cities worldwide, aiding users in specifying their flight details.

## Features
- Monitor specified flight prices for the next six months using Aviasales API
- Notify users on Telegram when a lower price is found
- Provide a comprehensive list of IATA codes for cities worldwide
- User-friendly interaction through Telegram using pyTelegramBotAPI

## Prerequisites
- Python 3.7+
- pip

## Setup
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/flight-price-tracker-bot.git
   cd flight-price-tracker-bot
   ```

2. Install the required dependencies:
   ```bash
    pip install pyTelegramBotAPI
    pip install python-dotenv
   ```

3. Set up your API keys:

   You'll need to obtain your own API keys from Aviasales and Telegram.

   Create a file named `config.py` in the project root, and add your API keys like so:
   ```python
   AVIASALES_API_KEY = 'your-aviasales-api-key'
   TELEGRAM_BOT_TOKEN = 'your-telegram-bot-token'
   ```
