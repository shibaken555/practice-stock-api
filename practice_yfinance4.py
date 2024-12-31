import yfinance as yf

# ティッカーシンボルを入力して合致した企業の株価をコンソールに出力させる
ticker_symbol = input("ティッカーシンボルを入力してください:")
print("入力されたティッカーシンボルは" + ticker_symbol)
input_ticker_symbol = yf.Ticker(ticker_symbol)
info = input_ticker_symbol.info
if info.get("address1") is None:
    print("情報が取得できませんでした。")
else:
    print(info)
    req_period = input("取得したい株価の期間を指定してください:")
    price = input_ticker_symbol.history(period=req_period)
    if price.empty:
     print("正確な期間を入力してください")
    else:
     print(price)
     price_data = price.to_dict()
     print(price_data)