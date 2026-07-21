def detect_fvg(df):

    bullish = []
    bearish = []

    for i in range(2, len(df)):

        high_1 = df["high"].iloc[i-2]
        low_3 = df["low"].iloc[i]

        low_1 = df["low"].iloc[i-2]
        high_3 = df["high"].iloc[i]

        # Bullish FVG
        if high_1 < low_3:
            bullish.append({
                "index": i,
                "top": low_3,
                "bottom": high_1
            })

        # Bearish FVG
        if low_1 > high_3:
            bearish.append({
                "index": i,
                "top": low_1,
                "bottom": high_3
            })

    return bullish, bearish