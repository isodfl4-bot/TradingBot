import ccxt

exchange = ccxt.binance({
    "enableRateLimit": True
})


def get_ohlcv(symbol, timeframe, limit=300):
    return exchange.fetch_ohlcv(
        symbol=symbol,
        timeframe=timeframe,
        limit=limit
    )