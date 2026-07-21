from scanner import get_ohlcv
from config import SYMBOLS, TIMEFRAMES

from indicators import prepare_dataframe
from strategy import get_trend

from market_structure import find_swings
from bos import detect_bos

from choch import detect_choch
from fvg import detect_fvg
for symbol in SYMBOLS:

    print("=" * 60)
    print(symbol)

    for tf in TIMEFRAMES:

        candles = get_ohlcv(symbol, tf)

        df = prepare_dataframe(candles)

        trend = get_trend(df)

        close = df["close"].iloc[-1]

        swing_highs, swing_lows = find_swings(df)

bos = detect_bos(df, swing_highs, swing_lows)

print(
    f"{tf} | Close:{close} | Trend:{trend} | {bos}"
)
choch = detect_choch(df, swing_highs, swing_lows)

print(
    f"{tf} | Close:{close} | Trend:{trend} | {bos} | {choch}"
)
bullish_fvg, bearish_fvg = detect_fvg(df)

print(f"Bullish FVG : {len(bullish_fvg)}")

print(f"Bearish FVG : {len(bearish_fvg)}")