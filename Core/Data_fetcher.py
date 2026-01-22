import requests, json
from Utils.Utility import BASE_URL, COINGECKO_API_KEY
from datetime import datetime


def fetch_current_price(coin_id):
    url = f"{BASE_URL}/simple/price"
    headers = {"x-cg-api-key": COINGECKO_API_KEY}
    params = {
        "ids": coin_id,
        "vs_currencies": "usd"
    }
    r = requests.get(url, headers=headers, params=params)
    data = r.json()

    if coin_id not in data:
        raise Exception(f"API Error: {data}")

    return data[coin_id]["usd"]

def fetch_historical_prices(coin_id, days=30):
    url = f"{BASE_URL}/coins/{coin_id}/market_chart"
    headers = {"x-cg-api-key": COINGECKO_API_KEY}
    params = {
        "vs_currency": "usd",
        "days": days
    }
    r = requests.get(url, headers=headers, params=params)
    data = r.json()

    if 'prices' not in data:
        raise Exception(f"API Error: {data}")

    return [price[1] for price in data['prices']]

#def price_info(coin_id):
#     import requests
#     params = {
#         "ids": coin_id,
#         "vs_currencies": "usd",
#         "include_7d_change": "true"
#     }
#     
#     data = requests.get(
#         "https://api.coingecko.com/api/v3/simple/price",
#         params=params
#     ).json()
#     
#     for coin, info in data.items():
#         print(f"{coin.upper()}")
#         print(f"  Harga: ${info['usd']}")
#         print(f"  24 Jam: {info['usd_24hr_change']:.2f}%\n")
# 
# url = "https://api.coingecko.com/api/v3/simple/price"
# 
# params = {
#     "ids": "ethereum",
#     "vs_currencies": "usd",
#     "include_24hr_change": "true",
#     "include_7d_change": "true",
#     "include_30d_change": "true"
# }
# 
# data = requests.get(url, params=params).json()
# 
# eth = data["ethereum"]
# 
# print(f"Harga ETH: ${eth['usd']}")
# print(f"24 Jam: {eth['usd_24h_change']:.2f}%")
# print(f"7 Hari: {eth['usd_7d_change']:.2f}%")
# print(f"30 Hari: {eth['usd_30d_change']:.2f}%")

if __name__ == '__main__':
    price_info("bitcoin")