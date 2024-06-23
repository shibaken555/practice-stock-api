import yfinance as yf

# 株価を取得したいティッカーシンボルを指定
# 以下はマイクロソフトのティッカーシンボルを指定した場合
msft = yf.Ticker("MSFT")
ivv = yf.Ticker("IVV")

# 指定した企業の情報が出力される
info = msft.info

# 指定した期間の企業の株価の情報が取得できる
# 指定できる期間は以下の通り
# ['1d', '5d', '1mo', '3mo', '6mo', '1y', '2y', '5y', '10y', 'ytd', 'max']
hist = msft.history(period="3mo")
# show meta information about the history (requires history() to be called first)
histmeta = msft.history_metadata

# 以下の3つの内容を出力
# 1株あたりの配当金、株式分割、キャピタルゲイン(投資信託、ETFのみ)
actions = msft.actions

# 1株あたりの配当金
dividens = msft.dividends

splists = msft.splits

# 投資信託、ETFのみ利用可能
capital_gains = ivv.capital_gains  # only for mutual funds & etfs

# 発行済み株式数を表示
count = msft.get_shares_full(start="2024-01-01", end="2024-06-01")

# 財務諸表を表示
# 損益計算(P/L)書を表示
income = msft.income_stmt

# 四半期の損益計算(P/L)書を表示
quarterly_income = msft.quarterly_income_stmt

# 貸借対照表を表示
balance_sheet = msft.balance_sheet
# 四半期の貸借対照表を表示
quarterly_balance_sheet = msft.quarterly_balance_sheet
# キャッシュフロー計算書を表示
cashflow = msft.cashflow
# 四半期のキャッシュフロー計算書を表示
quarterly_cashflow = msft.quarterly_cashflow

# 株主の情報を表示

# 主要株主の情報を表示
major_holders = msft.major_holders

# 主要株主(機関投資家)の情報を表示
institutional_holders = msft.institutional_holders

# 主要株主(投資信託)の情報を表示
mutualfund_holders = msft.mutualfund_holders

# 企業内部の人物の株の取引情報を表示
insider_transactions = msft.insider_transactions

# 企業内部の人物の売買情報を表示
insider_purchases = msft.insider_purchases

# 企業内部の人物の株主情報を表示
insider_roster_holders = msft.insider_roster_holders

# 推奨情報を表示
recommendations = msft.recommendations
recommendations_summary = msft.recommendations_summary
upgrades_downgrades = msft.upgrades_downgrades

# 1株あたりの利益そ表示。将来および過去の収益期日を表示し、デフォルトでは最大で今後4四半期および過去8四半期の収益を返す
# より多くの情報が必要な場合は、msft.get_earnings_dates(limit=XX) を使用し、limit 引数を増やしてください。
earnings_dates=msft.earnings_dates

# ISIN codeを表示
isin=msft.isin

# オプションの満了日を表示
options=msft.options

# 最新のニュースを表示
news = msft.news

# 特定の有効期限のオプション満了日の情報を表示
# コールとプットの情報を表示
opt = msft.option_chain("2024-06-28")
