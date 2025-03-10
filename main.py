from stock_data import get_stock_data
from stock_visualization import plot_stock_prices
from stock_prediction import predict_stock_price

# 종목 선택
stocks = ['005930.KQ', 'AAPL', 'TSLA']
data = get_stock_data(stocks)

# 주가 비교 그래프 출력
plot_stock_prices(data)

# 애플 주가 예측 실행
predict_stock_price(data, 'AAPL')
