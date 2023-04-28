import time
from binance.client import Client

# Set the API keys and symbol
api_key = 'YOUR_API_KEY'
api_secret = 'YOUR_API_SECRET'
symbol = 'BTCUSDT'
resistance_level = 50000
support_level = 45000

# Initialize the Binance client
client = Client(api_key, api_secret)

# Define the Breakout Bot function
def breakout_bot():
    try:
        # Get the current price of the symbol
        ticker = client.get_symbol_ticker(symbol=symbol)
        price = float(ticker['price'])
        
        # Check if the price has broken out above the resistance level
        if price > resistance_level:
            # Buy the symbol at the current price
            order = client.create_order(
                symbol=symbol,
                side=Client.SIDE_BUY,
                type=Client.ORDER_TYPE_MARKET,
                quantity=0.001
            )
            print(f'Bought {symbol} at {price}')
        
        # Check if the price has broken out below the support level
        if price < support_level:
            # Sell the symbol at the current price
            order = client.create_order(
                symbol=symbol,
                side=Client.SIDE_SELL,
                type=Client.ORDER_TYPE_MARKET,
                quantity=0.001
            )
            print(f'Sold {symbol} at {price}')
    except Exception as e:
        print(e)

# Set the interval to run the bot every minute
while True:
    breakout_bot()
    time.sleep(60)
