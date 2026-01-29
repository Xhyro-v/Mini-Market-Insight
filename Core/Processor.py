import numpy as np
from Utils.Utility import Color

def analyze_signal(current_price, avg_price):
    diff_percent = ((current_price - avg_price) / avg_price) * 100

    if diff_percent >= 7:
        signal = Color.Red("Strong Take Profit ")
    elif diff_percent >= 3:
        signal = Color.Yellow("Take Profit ")
    elif diff_percent <= -7:
        signal = Color.Red("Strong Cut Loss ")
    elif diff_percent <= -3:
        signal = Color.Green("Potential Entry ")
    else:
        signal = Color.Blue("Hold / Wait ")

    return signal, diff_percent