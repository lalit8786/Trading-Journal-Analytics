profits = [4.45 , 23.03 , -27.05 , -12.5 , -5.35 , 130.9 , 482.6 , 226 ]
for p in profits:
    print(p)
wins = 0
for p in profits:
    if p>0:
        wins = wins + 1
        print("Win: ", p)
print(wins)

total_won = 0
for p in profits:
    if p>0:
        total_won = total_won + p
print("total_won:", total_won)

loss = 0
for p in profits:
    if p<0:
        loss = loss + 1
        print("Loss: ", p)
print(loss)

total_loss = 0
for p in profits:
    if p<0:
        total_loss = total_loss + p
print("total_loss:", total_loss)



     









