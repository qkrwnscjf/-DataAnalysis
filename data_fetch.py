import yfinance as yf

def get_stock_data(ticker, period="6mo"):
    stock = yf.Ticker(ticker)
    df = stock.history(period=period)
    return df

if __name__ == "__main__":
    df = get_stock_data("PLTR")
    print(df.head())  # 데이터 확인
