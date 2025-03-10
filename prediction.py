import yfinance as yf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pmdarima import auto_arima

def predict_stock_price(stock_symbol, start_date="2025-3-01", end_date="2025-03-31", future_days=30):
    # 📌 1. 주식 데이터 불러오기
    data = yf.download(stock_symbol, start=start_date, end=end_date)
    
    # 📌 2. 종가(Close) 데이터 사용
    stock_prices = data['Close']

    # 📌 3. Auto ARIMA 모델 학습
    model = auto_arima(stock_prices, seasonal=True, stepwise=True, suppress_warnings=True)

    # 📌 4. 30일 뒤까지 예측
    forecast = model.predict(n_periods=future_days)

    # 📌 5. 날짜 생성
    future_dates = pd.date_range(start=data.index[-1], periods=future_days + 1, freq='B')[1:]

    # 📌 6. 그래프 시각화
    plt.figure(figsize=(12, 6))
    plt.plot(stock_prices.index, stock_prices, label="Actual Prices", color="blue")
    plt.plot(future_dates, forecast, label="Predicted Prices (Next 30 days)", color="red", linestyle="--")

    # 스타일링
    plt.title(f"{stock_symbol} Stock Price Prediction (Next {future_days} Days)", fontsize=16, fontweight="bold")
    plt.xlabel("Date")
    plt.ylabel("Stock Price")
    plt.xticks(rotation=45)
    plt.legend()
    plt.grid(True, linestyle="--", alpha=0.6)
    plt.show()

    return forecast
