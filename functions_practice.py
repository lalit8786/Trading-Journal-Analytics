def calculate_position_size(account_balance, risk_percentage, stop_loss, entry_price):
    risk_dollars = account_balance * (risk_percentage / 100)
    stop_distance = abs(entry_price - stop_loss)
    position_size = risk_dollars / stop_distance
    return position_size
result = calculate_position_size(5000 , 0.4 , 3995 , 3990)
print (result)

profits = [4.45 , 23.03 , -27.05 , -12.5 , -5.35 , 130.9 , 482.6 , 226 ]
def calculate_win_rate(profits):
    total_wins = 0
    total_trades = len(profits)
    for p in profits:
        if p > 0:
            total_wins = total_wins + 1
    winrate = (total_wins / total_trades) * 100
    return winrate
win_rate = calculate_win_rate(profits)
print("Win Rate: ", win_rate)
total_loss = 0
total_trades = len(profits)
for p in profits:
    if p < 0:
        total_loss = total_loss + 1

def calculate_expectancy(profits):
    total_wins = 0
    total_losses = 0
    total_profit = 0
    total_loss = 0
    for p in profits:
        if p > 0:
            total_wins = total_wins + 1
            total_profit = total_profit + p
        elif p < 0:
            total_losses = total_losses + 1
            total_loss = total_loss + p
    average_win = total_profit / total_wins
    average_loss = total_loss / total_losses
    win_rate = total_wins / len(profits) * 100
    loss_rate = 100 - win_rate
    expectancy = (win_rate/100 * average_win) + (loss_rate/100 * average_loss)
    return expectancy
expectancy = calculate_expectancy(profits)
print("Expectancy:", expectancy)






    



