import requests, json
from Utils.Utility import BASE_URL, COINGECKO_API_KEY


def fetch_current_price(coin_id):
    url = f"{BASE_URL}/simple/price"
    headers = {"x-cg-api-key": COINGECKO_API_KEY}
    params = {
        "ids": coin_id,
        "vs_currencies": "usd"
    }

    r = requests.get(url, headers=headers, params=params)
    return r.json()[coin_id]["usd"]


def fetch_historical_prices(coin_id, days=30):
    url = f"{BASE_URL}/coins/{coin_id}/market_chart"
    headers = {"x-cg-api-key": COINGECKO_API_KEY}
    params = {
        "vs_currency": "usd",
        "days": days
    }

    r = requests.get(url, headers=headers, params=params)
    prices = r.json()['prices']
    return [price[1] for price in prices]
