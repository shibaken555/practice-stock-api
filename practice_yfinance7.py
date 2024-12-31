import yfinance as yf

# 複数のティッカーシンボルが入力された事を想定した練習用のコード
list = ["MSFT", "AAPL", "GOOG"]
tickers = yf.Tickers(list)
# print(tickers)
for i in list:
    print(i)
    prices = tickers.tickers[i].history(period = "5d")
    print(prices)
    # price_data = prices.reset_index().to_dict(orient="records")
    # print(price_data)
# access each ticker using (example)
msft = tickers.tickers["MSFT"].info
aapl = tickers.tickers["AAPL"].history(period="5d")
goog = tickers.tickers["GOOG"].actions


dict_list = {"ticker_symbol": tickers}
# print(dict_list)
