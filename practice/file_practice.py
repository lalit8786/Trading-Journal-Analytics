import pandas as pd
trades = ["XAUUSD buy 50.5", "XAUUSD sell 20.3", "XAUUSD buy 75.0"]

with open("trade_log.txt", "w") as f:
    for trade in trades:
        f.write(trade + "\n")
with open("trade_log.txt", "r") as f:
    content = f.read()
    print(content)

df = pd.read_excel("ReportHistory-25858699.xlsx" ,skiprows=6)
df = df.iloc[0:8]
df.columns = ["open_time", "position_id", "symbol", "type", "volume", "open_price","sl", "tp", "close_time", "close_price", "commission", "swap", "profit", "extra"]
print(df)
with open("profit_log.txt", "w") as f:
    for value in df["profit"]:
        f.write(str(value) + "\n")

with open("profit_log.txt", "r") as f:
    content = f.read()
    print(content)
def save_summary_to_file(self, filename="summmary.txt"):
    if self.win_rate is None:
        print("Run calculate_all_stats() first.")
        return
    with open(filename, "w")as f:
        f.write ("-----Trading Journal Summary-----\n")
    f.write(f"Win Rate: {self.win_rate:.2f}%")
    f.write(f"Profit Factor: {self.profit_factor:.2f}\n")
    f.write(f"Expectancy: {self.expectancy:.2f}\n")
    f.write(f"Drawdown: {self.drawdown:.2f}\n")
    f.write("Session Breakdown:\n")
    f.write(self.session_stats)
