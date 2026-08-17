#trading risk calculator
account_balance = 5000
risk_percent = 0.4
try:
 entry = float(input("enter your entry price:"))
 stop_loss = float(input("enter your stop_loss price:"))
 risk_dollars = account_balance * risk_percent / 100
 stop_distance = abs(entry - stop_loss)
 position_size = risk_dollars / stop_distance
 print("risk in dollars:",risk_dollars)
 print("stop distance:",stop_distance)
 print("position size:",position_size)
except:
 print("Invalid Input.Please enter numbers only.")
 