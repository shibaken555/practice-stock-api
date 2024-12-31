import yfinance as yf

# ティッカーシンボルを入力して合致した企業の情報をコンソールに出力させる
print("ティッカーシンボルを入力してください")
ticker_symbol = input()
print("入力されたティッカーシンボルは" + ticker_symbol)
input_ticker_symbol = yf.Ticker(ticker_symbol)
info = input_ticker_symbol.info
if info.get("trailingPegRatio") is None:
    print("情報が取得できませんでした。")
else:
    print(info)
