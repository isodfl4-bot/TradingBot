def detect_choch(df, swing_highs, swing_lows):

    close = df["close"].iloc[-1]

    if len(swing_highs) < 2 or len(swing_lows) < 2:
        return "No CHOCH"

    prev_high = df["high"].iloc[swing_highs[-2]]
    last_high = df["high"].iloc[swing_highs[-1]]

    prev_low = df["low"].iloc[swing_lows[-2]]
    last_low = df["low"].iloc[swing_lows[-1]]

    # Bullish CHOCH
    if last_low > prev_low and close > last_high:
        return "Bullish CHOCH"

    # Bearish CHOCH
    if last_high < prev_high and close < last_low:
        return "Bearish CHOCH"

    return "No CHOCH"