def detect_bos(df, swing_highs, swing_lows):

    close = df["close"].iloc[-1]

    last_high = None
    last_low = None

    if swing_highs:
        last_high = df["high"].iloc[swing_highs[-1]]

    if swing_lows:
        last_low = df["low"].iloc[swing_lows[-1]]

    if last_high and close > last_high:
        return "Bullish BOS"

    if last_low and close < last_low:
        return "Bearish BOS"

    return "No BOS"