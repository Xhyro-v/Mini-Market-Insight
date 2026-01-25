import requests, json
from Utils.Utility import crypto

def fetch_current_price(coin_id,COINGECKO_API_KEY):
    BASE_URL = crypto.url()
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

def fetch_historical_prices(coin_id, COINGECKO_API_KEY, days=30,):
    BASE_URL = crypto.url()
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


def Global_market(vs_currency="usd"):
    url = crypto.global_url()# "https://api.coingecko.com/api/v3/global"
    
    try:
        res = requests.get(url, timeout=10)
        res.raise_for_status()
        data = res.json()["data"]

        market_cap = data["total_market_cap"][vs_currency]
        volume = data["total_volume"][vs_currency]

        return {
            "market_cap": market_cap,
            "volume": volume
        }

    except Exception as e:
        return {
            "error": str(e)
        }  
