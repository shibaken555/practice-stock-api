import yfinance as yf
import pandas as pd

# 複数の企業のティッカーシンボルを扱うコードのサンプル
tickers = yf.Tickers('MSFT AAPL GOOG')

tickers.tickers['MSFT'].info
yf.download(['MSFT', 'AAPL', 'GOOG'], period='1mo')

# access each ticker using (example)
msft = tickers.tickers["MSFT"].info
aapl = tickers.tickers["AAPL"].history(period="1mo")
goog = tickers.tickers["GOOG"].actions

print(type(msft))