# Trading Journal Analytics

A Python tool built for traders to analyze their trading history and 
track performance over time. It takes real MT5 trade export data and 
calculates the core stats every trader should track — win rate, 
profit factor, expectancy, drawdown, and more.

## What it does
- Calculates risk and position size for a given trade
- Tracks wins, losses, average win, and average loss
- Calculates win rate and loss rate
- Calculates profit factor (total won ÷ total lost)
- Calculates expectancy (average $ made per trade)
- Identifies your best and worst trade
- Tracks account equity curve and max drawdown

## How it works
The script reads a trade history report exported directly from MT5 
(Excel format), cleans up the raw export (MT5 reports include extra 
header rows and multiple stacked tables), and loads it into a pandas 
DataFrame. From there, it filters and aggregates the data to calculate 
each statistic.

## Object-Oriented Version
`trading_journal.py` refactors the core analytics into a `TradingJournal` 
class — the same calculations as `Journal_analytics.py`, restructured 
around state instead of a single function returning a dictionary.

```python
journal = TradingJournal(df)
journal.calculate_all_stats()
journal.print_summary()
```

Each stat (win rate, profit factor, expectancy, drawdown) is calculated 
by its own method and stored as an attribute on the object, making it 
easier to extend with new metrics later. The class also classifies each 
trade by session — London or New York, based on the trade's open hour — 
and breaks down average profit per session using `groupby`.

## Sample output
winrate: 62.5
win_average: 173.4
loss_average: -14.97
profit_factor: 19.31
loss_rate: 37.5
expectancy: 102.76
max_drawdown: -44.9

best_trade: XAUUSD buy, 2026.08.07, profit: 482.6
worst_trade: XAUUSD buy, 2026.08.03, profit: -27.05
## What I learned
This was my first project where I understood every line of code I wrote, 
rather than just getting a working result. Debugging pandas syntax — 
filtering, column renaming, cumulative sums — took some trial and error, 
but that process is what actually taught me how pandas works.