import pandas as pd
try:
 df = pd.read_excel("ReportHistory-2585869.xlsx" ,skiprows=6)
 df = df.iloc[0:8]
 df.columns = ["open_time", "position_id", "symbol", "type", "volume", "open_price","sl", "tp", "close_time", "close_price", "commission", "swap", "profit", "extra"]
 print(df)
 win = df[df["profit"] > 0]
 print(len(win))
 print(len(df))
 winrate = len(win)/len(df)*100
 print("winrate:",winrate)
 win_average = win["profit"].mean()
 print("win_average:",round(win_average, 2))
 loss = df[df["profit"] < 0]
 loss_average = loss["profit"].mean()
 print("loss_average:",round(loss_average, 2))
 total_won = win["profit"].sum()
 total_loss = loss["profit"].sum()
 profit_factor = total_won/abs(total_loss)
 print("profit_factor:",round(profit_factor, 2))
 best_trade = df[df["profit"] == df["profit"].max()]
 worst_trade = df[df["profit"] == df["profit"].min()]
 print("best_trade:",best_trade)
 print("worst_trade:",worst_trade)
 loss_rate = 100-winrate
 print("loss_rate:",round(loss_rate, 2))
 expectancy =(winrate/100*win_average)+(loss_rate/100*loss_average)
 print("expectancy:",round(expectancy,2))
 df["running_balance"] = df["profit"].cumsum()
 print(df["running_balance"].round(2))
 df["peak"] = df["running_balance"].cummax()
 print(df["peak"].round(2))
 df["drawdown"] = df["running_balance"] - df["peak"]
 print(df["drawdown"].round(2))
 max_drawdown = df["drawdown"].min()
 print("max_drawdown:",round(max_drawdown,2))
except:
 print("Could not load the Trade Report.Check the file name and make sure it's not open in Excel")