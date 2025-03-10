import pandas as pd
import matplotlib.pyplot as plt

# 이동평균 계산
def add_moving_averages(df):
    df["MA50"] = df["Close"].rolling(window=50).mean()
    df["MA200"] = df["Close"].rolling(window=200).mean()
    return df

# RSI 계산
def compute_rsi(data, window=14):
    delta = data.diff()
    gain = (delta.where(delta > 0, 0)).rolling(window=window).mean()
    loss = (-delta.where(delta < 0, 0)).rolling(window=window).mean()
    rs = gain / loss
    rsi = 100 - (100 / (1 + rs))
    return rsi

if __name__ == "__main__":
    from data_fetch import get_stock_data
    df = get_stock_data("PLTR")

    df = add_moving_averages(df)
    df["RSI"] = compute_rsi(df["Close"])

    print(df.tail())  # 분석 데이터 확인
