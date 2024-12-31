import yfinance as yf
import pandas as pd

# 対象の変数がDataFrameかどうかを判定する
# サンプルのDataFrame
df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})

# DataFrameかどうかをチェック
if isinstance(df, pd.DataFrame):
    print("dfはDataFrameです。")
else:
    print("dfはDataFrameではありません。")
