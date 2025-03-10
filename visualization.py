import matplotlib.pyplot as plt

def plot_stock_data(df, title="Stock Price"):
    plt.figure(figsize=(12,6))
    plt.plot(df["Close"], label="Closing Price", color="blue")
    plt.title(title)
    plt.xlabel("Date")
    plt.ylabel("Price (USD)")
    plt.legend()
    plt.show(block=True)



if __name__ == "__main__":
    from data_fetch import get_stock_data
    df = get_stock_data("PLTR")
    plot_stock_data(df, "Palantir Stock Price")
