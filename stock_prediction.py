import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

def predict_stock_price(data, stock_name):
    data['Days'] = np.arange(len(data))
    X = data[['Days']]
    y = data[stock_name]

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, shuffle=False)
    model = LinearRegression()
    model.fit(X_train, y_train)

    future_days = np.arange(len(data), len(data) + 30).reshape(-1, 1)
    predictions = model.predict(future_days)

    plt.figure(figsize=(12,6))
    plt.plot(data.index, data[stock_name], label=f'Actual {stock_name} Price')
    plt.plot(pd.date_range(start=data.index[-1], periods=30, freq='D'), predictions, label='Predicted Price', linestyle='dashed', color='red')
    plt.title(f"{stock_name} 주가 예측")
    plt.xlabel("날짜")
    plt.ylabel("주가 ($)")
    plt.legend()
    plt.show()
