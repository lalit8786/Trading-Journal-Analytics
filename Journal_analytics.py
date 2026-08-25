import pandas as pd
def calculate_all_stats(df):
    win = df[df["profit"] > 0]
    loss = df[df["profit"] < 0]
    
    winrate = len(win) / len(df) * 100
    loss_rate = 100 - winrate
    win_average = win["profit"].mean()
    loss_average = loss["profit"].mean()
    total_won = win["profit"].sum()
    total_loss = loss["profit"].sum()
    profit_factor = total_won / abs(total_loss)
    expectancy = (winrate/100 * win_average) + (loss_rate/100 * loss_average)
    running_balance = df["profit"].cumsum()
    peak = running_balance.cummax()
    drawdown = running_balance - peak
    max_drawdown = drawdown.min()
    best_trade = df[df["profit"] == df["profit"].max()]
    worst_trade = df[df["profit"] == df["profit"].min()]
    
    stats = {
        "winrate": round(winrate, 2),
        "win_average": round(win_average, 2),
        "loss_average": round(loss_average, 2),
        "profit_factor": round(profit_factor, 2),
        "expectancy": round(expectancy, 2),
        "max_drawdown": round(max_drawdown, 2),
        "best_trade": best_trade,
        "worst_trade": worst_trade
    }
    return stats
try:
 df = pd.read_excel("ReportHistory-25858699.xlsx" ,skiprows=6)
 df = df.iloc[0:8]
 df.columns = ["open_time", "position_id", "symbol", "type", "volume", "open_price","sl", "tp", "close_time", "close_price", "commission", "swap", "profit", "extra"]
 print(df)
 df["open_time"] = pd.to_datetime(df["open_time"])
 df["hour"] = df["open_time"].dt.hour
 print(df[["open_time", "hour"]])
 def get_session(hour):
  if hour >= 7 and hour < 11:
   return "London"
  elif hour >= 13 and hour < 17:
    return "New York"
  else:
    return "Other"
 df["session"] = df["hour"].apply(get_session)
 print(df[["open_time", "hour", "session"]])
 session_stats = df.groupby("session")["profit"].mean()
 print(session_stats)
 stats = calculate_all_stats(df)
 print(stats)
except:
 print("Could not load the Trade Report.Check the file name and make sure it's not open in Excel")