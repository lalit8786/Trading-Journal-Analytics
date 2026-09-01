import pandas as pd
class TradingJournal:
    def __init__(self , df):
        self.df = df
        self.win_rate = None
        self.profit_factor = None
        self.expectancy = None
        self.drawdown = None
        self.session_stats= None
        self.best_trade = None
        self.worst_trade = None

    def calculate_all_stats(self):
        self.calculate_win_rate()
        self.calculate_profit_factor()
        self.calculate_expectancy()
        self.calculate_drawdown()
        self.classify_session()
        self.find_best_worst_trade()
        
    def calculate_win_rate(self):
        win = self.df[self.df["profit"] > 0]
        self.win_rate = len(win) / len(self.df) * 100

    def calculate_profit_factor(self):
        win = self.df[self.df["profit"] > 0]
        loss = self.df[self.df["profit"] < 0]
        total_won = win["profit"].sum()
        total_loss = loss["profit"].sum()
        self.profit_factor = total_won / abs(total_loss)

    def calculate_expectancy(self):
        win = self.df[self.df["profit"] > 0]
        loss = self.df[self.df["profit"] < 0]
        winrate = len(win) / len(self.df) * 100
        loss_rate = 100 - winrate
        win_average = win["profit"].mean()
        loss_average = loss["profit"].mean()
        self.expectancy = (winrate/100 * win_average) + (loss_rate/100 * loss_average)

    def calculate_drawdown(self):
        running_balance = self.df["profit"].cumsum()
        peak = running_balance.cummax()
        drawdown = running_balance - peak
        self.drawdown = drawdown.min()

    def classify_session(self):
        self.df["open_time"] = pd.to_datetime(self.df["open_time"])
        self.df["hour"] = self.df["open_time"].dt.hour
        def get_session(hour):
            if hour >= 7 and hour < 11:
                return "London"
            elif hour >= 13 and hour < 17:
                return "New York"
            else:
                return "Other"
        self.df["session"] = self.df["hour"].apply(get_session)
        self.session_stats = self.df.groupby("session")["profit"].mean()
    def log_trades(self,trade_dict):
        new_row_df = pd.DataFrame([trade_dict])
        self.df = pd.concat([self.df, new_row_df], ignore_index=True)
        self.calculate_all_stats()
    def undo_last_trade(self):
        if len(self.df) == 0:
            print("No trades to remove.") 
            return
        self.df = self.df.iloc[:-1]
        self.calculate_all_stats()
    def find_best_worst_trade(self):
        best_index = self.df["profit"].idxmax()
        self.best_trade = self.df.loc[best_index]
        worst_index = self.df["profit"].idxmin()
        self.worst_trade = self.df.loc[worst_index]
    def print_summary(self):
        if self.win_rate is None:
            print("Run calculate_all_stats() first.")
            return
        print("----- Trading Journal Summary -----")
        print(f"Win Rate: {self.win_rate:.2f}%")
        print(f"Profit Factor: {self.profit_factor:.2f}")
        print(f"Expectancy: {self.expectancy:.2f}")
        print(f"Drawdown: {self.drawdown:.2f}")
        print("Session Breakdown:")
        print(self.session_stats)
    def save_summary_to_file(self, filename="summary.txt"):
        if self.win_rate is None:
            print("Run calculate_all_stats() first.")
            return
        with open(filename, "w")as f:
         f.write ("-----Trading Journal Summary-----\n")
         f.write(f"Win Rate: {self.win_rate:.2f}%\n")
         f.write(f"Profit Factor: {self.profit_factor:.2f}\n")
         f.write(f"Expectancy: {self.expectancy:.2f}\n")
         f.write(f"Drawdown: {self.drawdown:.2f}\n")
         f.write("Session Breakdown:\n")
         f.write(self.session_stats.to_string())
         f.write("\nBest Trade:\n")
         f.write(self.best_trade.to_string())
         f.write("\nWorst Trade:\n")
         f.write(self.worst_trade.to_string())
df = pd.read_excel("ReportHistory-25858699.xlsx", skiprows=6)
df = df.iloc[0:8]
df.columns = ["open_time", "position_id", "symbol", "type", "volume", "open_price","sl", "tp", "close_time", "close_price", "commission", "swap", "profit", "extra"]
journal = TradingJournal(df)
journal.calculate_all_stats()
print("Before:",journal.win_rate)
journal.print_summary()
journal.save_summary_to_file()
journal.log_trades({"open_time":"2026-08-27 10:00:00", "profit":550.00})
print ("after:",journal.win_rate)
journal.undo_last_trade()
print("After undoing last trade:",journal.win_rate)
journal.find_best_worst_trade()
print("Best Trade:\n",journal.best_trade)
print("Worst Trade:\n",journal.worst_trade)
while True:
    print("1. View Summary")
    print("2. Log a Trade")
    print("3. Undo Last Trade")
    print("4. Exit")
    choice = input("Choose an option: ")

    if choice == "1":
        journal.print_summary()
    elif choice == "2":
        open_time = input("Enter open time (YYYY-MM-DD HH:MM:SS): ")
        profit = float(input("Enter profit: "))
        trade_dict = {"open_time": open_time, "profit": profit}
        journal.log_trades(trade_dict)
    elif choice == "3":
        journal.undo_last_trade()
    elif choice == "4":
        break
    else:
        print("Invalid option, try again.")