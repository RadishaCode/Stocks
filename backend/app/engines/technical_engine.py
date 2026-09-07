import pandas as pd


def calculate_ma(series, period):
    return series.rolling(period).mean()


def calculate_rsi(series, period=14):
    delta = series.diff()
    gain = delta.where(delta > 0, 0).rolling(period).mean()
    loss = -delta.where(delta < 0, 0).rolling(period).mean()
    rs = gain / loss
    return 100 - (100 / (1 + rs))


def analyze(close):
    ma20 = calculate_ma(close,20).iloc[-1]
    ma50 = calculate_ma(close,50).iloc[-1]
    rsi = calculate_rsi(close).iloc[-1]

    score = 50

    if close.iloc[-1] > ma20:
        score += 15
    if close.iloc[-1] > ma50:
        score += 15
    if 50 < rsi < 70:
        score += 10

    return {
        'ma20': float(ma20),
        'ma50': float(ma50),
        'rsi': float(rsi),
        'score': min(score,100)
    }
