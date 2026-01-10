from Utils.Utility import Input, Color, Center, CRYPTO_LIST, BASE_URL, COINGECKO_API_KEY
from Core.Data_fetcher import fetch_current_price, fetch_historical_prices
from Core.Processor import analyze_signal


current_price = fetch_current_price(CRYPTO_LIST)
historical_prices = fetch_historical_prices(CRYPTO_LIST, days=7)
signal, avg_price, diff = analyze_signal(current_price, historical_prices)


print(f"Crypto         : {CRYPTO_LIST[0]}")
print(f"Current Price : {Color.Green('$')}"+f"{Color.Green(current_price)}")
print(f"7D Average    : ${avg_price:.2f}")
print(f"Signal        : {signal}")
print(f"Diff          : {diff:.2f}%")
