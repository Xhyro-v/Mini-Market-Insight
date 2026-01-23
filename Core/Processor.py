import numpy as np
from Utils.Utility import Color, Input

def analyze_signal(current_price, historical_prices, avg_price):
    diff_percent = ((current_price - avg_price) / avg_price) * 100

    if diff_percent > 3:
        signal = f"{Color.Red('Consider profit')}"
    elif diff_percent < -3:
        signal = f"{Color.Green('Consider entry')}"
    else:
        signal = f"{Color.Yellow('Hold/Wait')}"

    return signal, avg_price, diff_percent
