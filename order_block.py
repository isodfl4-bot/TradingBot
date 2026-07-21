def detect_order_blocks(df):

    bullish = []
    bearish = []

    for i in range(2, len(df)-1):

        current = df.iloc[i]
        nxt = df.iloc[i+1]

        # Bullish Order Block
        if (
            current["close"] < current["open"] and
            nxt["close"] > current["high"]
        ):

            bullish.append({
                "index": i,
                "high": current["high"],
                "low": current["low"]
            })

        # Bearish Order Block
        if (
            current["close"] > current["open"] and
            nxt["close"] < current["low"]
        ):

            bearish.append({
                "index": i,
                "high": current["high"],
                "low": current["low"]
            })

    return bullish, bearish