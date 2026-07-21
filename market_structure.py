import pandas as pd

def find_swings(df, left=3, right=3):
    swing_highs = []
    swing_lows = []

    highs = df["high"].tolist()
    lows = df["low"].tolist()

    for i in range(left, len(df) - right):

        if highs[i] == max(highs[i-left:i+right+1]):
            swing_highs.append(i)

        if lows[i] == min(lows[i-left:i+right+1]):
            swing_lows.append(i)

    return swing_highs, swing_lows