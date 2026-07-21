import pandas as pd

def prepare_dataframe(ohlcv):

    df = pd.DataFrame(
        ohlcv,
        columns=[
            "time",
            "open",
            "high",
            "low",
            "close",
            "volume"
        ]
    )

    df["EMA20"] = df["close"].ewm(span=20).mean()

    df["EMA50"] = df["close"].ewm(span=50).mean()

    df["EMA200"] = df["close"].ewm(span=200).mean()

    return df