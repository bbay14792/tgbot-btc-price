import requests
import time
import telegram

# Replace with your own Telegram bot token and chat ID
bot_token = 'your_bot_token'
chat_id = 'your_chat_id'

# Function to get the current Bitcoin price using CoinGecko API
def get_btc_price():
    response = requests.get('https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd')
    btc_price = response.json()['bitcoin']['usd']
    return btc_price

# Initialize Telegram bot
bot = telegram.Bot(token=bot_token)

# Loop to send Bitcoin price every hour
while True:
    btc_price = get_btc_price()
    bot.send_message(chat_id=chat_id, text=f'Current Bitcoin price: ${btc_price}')
    time.sleep(3600)  # Sleep for one hour before sending next message
