trades = [
    {"symbol": "XAUUSD", "profit": 428.6, "type": "Buy"},
    {"symbol": "XAUUSD", "profit": 4.45, "type": "buy"},
    {"symbol": "XAUUSD", "profit": -27.05, "type": "buy"},
    {"symbol": "XAUUSD", "profit": 482.6, "type": "buy"}
]
for trade in trades:
    print(trade["symbol"], trade["profit"], trade["type"])
    print()
wins = 0
losses = 0
for trade in trades:
    if trade["profit"] > 0:
        wins = wins + 1
    else:
        losses = losses + 1
print("Wins:", wins)
print("Losses:", losses)
def calculate_win_rate(trades):
 win = 0
 for trade in trades:
    if trade["profit"] > 0:
            win = win + 1
    win_rate = win / len(trades) * 100 if trades else 0
 return win_rate
win_rate = calculate_win_rate(trades)
print("win rate:", win_rate)
def calculate_stats(trades):
 wins = 0
 losses = 0
 total_profit = 0
 total_loss = 0
 for trade in trades:
     if trade["profit"] > 0:
         wins = wins + 1
         total_profit = total_profit + trade["profit"]
     else:
      if trade["profit"] < 0:    
         losses = losses + 1
         total_loss = total_loss + trade["profit"]
 win_rate = wins / len(trades) * 100
 loss_rate = 100 - win_rate
 average_win = total_profit / wins
 average_loss = total_loss / losses
 expectancy = (win_rate/100 * average_win) + (loss_rate/100 * average_loss)
 return expectancy
calculate_stats = calculate_stats(trades)
print("calculate_stats:" , calculate_stats)