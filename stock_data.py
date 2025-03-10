import yfinance as yf

def get_stock_data(stocks, start="2023-01-01", end="2024-01-01"):
    return yf.download(stocks, start=start, end=end)['Adj Close']


