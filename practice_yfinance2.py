import yfinance as yf

tickers = yf.Tickers(["msft", "aapl", "goog"])

# access each ticker using (example)
msft = tickers.tickers["MSFT"].info
aapl = tickers.tickers["AAPL"].history(period="1mo")
goog = tickers.tickers["GOOG"].actions

print(msft)
print(aapl)
print(goog)
