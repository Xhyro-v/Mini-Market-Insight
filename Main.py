import time
from Utils.Utility import Input, Color, Center
from Core.Data_fetcher import fetch_current_price, fetch_historical_prices
from Core.Processor import analyze_signal

CRYPTO_LIST = [
    "bitcoin",
    "ethereum",
    "solana",
    "binancecoin"
]

print(Center.box("CRYPTO SIGNAL ANALYZER"))
for i, coin in enumerate(CRYPTO_LIST, 1):
    print(f"{i}. {coin}")

choice = int(Input.number("\nPilih Crypto (1-4): "))
coin_id = CRYPTO_LIST[choice - 1]

while True:
    current_price = fetch_current_price(coin_id)
    historical_prices = fetch_historical_prices(coin_id, days=30)
    
    signal, avg_price, diff = analyze_signal(current_price, historical_prices)
    
    print("\n" + Center.box("RESULT"))
    print(f"Crypto         : {coin_id}")
    print(f"Current Price  : {Color.Green('$')}{Color.Green(current_price)}")
    print(f"7D Average     : ${avg_price:.2f}")
    print(f"Signal         : {signal}")
    print(f"Diff           : {diff:.2f}%")
