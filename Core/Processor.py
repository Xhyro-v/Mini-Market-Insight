import numpy as np
from Utils.Utility import Color

def analyze_signal(current_price, historical_prices):
    prices = np.array(historical_prices)
    avg_price = prices.mean()

    diff_percent = ((current_price - avg_price) / avg_price) * 100

    if diff_percent > 3:
        signal = f"{Color.Red('SELL')}"
    elif diff_percent < -3:
        signal = f"{Color.Green('BUY')}"
    else:
        signal = f"{Color.Yellow('HOLD')}"

    return signal, avg_price, diff_percent
