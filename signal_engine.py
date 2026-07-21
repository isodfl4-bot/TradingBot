from strategy import get_trend
from market_structure import find_swings
from bos import detect_bos
from choch import detect_choch
from fvg import detect_fvg
from order_block import detect_order_blocks


def generate_signal(df):

    trend = get_trend(df)

    swing_highs, swing_lows = find_swings(df)

    bos = detect_bos(df, swing_highs, swing_lows)

    choch = detect_choch(df, swing_highs, swing_lows)

    bullish_fvg, bearish_fvg = detect_fvg(df)

    bullish_ob, bearish_ob = detect_order_blocks(df)

    signal = {
        "trend": trend,
        "bos": bos,
        "choch": choch,
        "bullish_fvg": len(bullish_fvg),
        "bearish_fvg": len(bearish_fvg),
        "bullish_ob": len(bullish_ob),
        "bearish_ob": len(bearish_ob),
        "buy": False,
        "sell": False,
        "score": 0
    }

    if trend == "BULLISH":
        signal["score"] += 30

    if bos == "Bullish BOS":
        signal["score"] += 25

    if choch == "Bullish CHOCH":
        signal["score"] += 20

    if len(bullish_fvg):
        signal["score"] += 25

    if len(bullish_ob):
        signal["score"] += 15

    if signal["score"] >= 80:
        signal["buy"] = True

    return signal