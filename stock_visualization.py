import matplotlib.pyplot as plt

def plot_stock_prices(data):
    plt.figure(figsize=(12,6))
    for stock in data.columns:
        plt.plot(data.index, data[stock], label=stock)

    plt.title("주식 가격 비교")
    plt.xlabel("날짜")
    plt.ylabel("주가 ($)")
    plt.legend()
    plt.show()

