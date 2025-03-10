
from data_fetch import get_stock_data
from visualization import plot_stock_data
from analysis import add_moving_averages, compute_rsi
from prediction import predict_stock_price

# 주식 티커 설정
TICKER = "PLTR"

def main():
    # 1. 데이터 가져오기
    print(f"Fetching data for {TICKER}...")
    df = get_stock_data(TICKER)

    # 2. 데이터 시각화
    print("Plotting stock price chart...")
    plot_stock_data(df, f"{TICKER} Stock Price")

    # 3. 기술적 분석
    print("Performing technical analysis...")
    df = add_moving_averages(df)
    df["RSI"] = compute_rsi(df["Close"])
    
    # 4. 주가 예측
    print("Predicting future stock prices...")
    predict_stock_price(df)

if __name__ == "__main__":
    main()
