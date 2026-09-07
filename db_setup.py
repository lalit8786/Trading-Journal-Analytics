import pandas as pd
import sqlite3
conn = sqlite3.connect("trading_journal.db")
cursor = conn.cursor()
cursor.execute('''CREATE TABLE trades (
    open_time TEXT,
    position_id INTEGER,
    symbol TEXT,
    type TEXT,
    volume REAL,
    open_price REAL,    
    sl REAL,
    tp REAL,    
    close_time TEXT,    
    close_price REAL,
    commission REAL,
    swap REAL,
    profit REAL,
    extra TEXT
                )''')
cursor.execute("INSERT INTO trades (open_time, position_id,symbol, type, volume, open_price, sl, tp, close_time, close_price, commission, swap, profit, extra) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", 
               ("2026-09-02 17:42:33", 1, "XAUUSD", "SELL", 0.05, 4385.39, 4388.16, 4375.07, "2026-09-02 15:00:00", 4385.08, 0.25, 0, 1.55, None))
conn.commit()
cursor.execute("SELECT * FROM trades")
rows = cursor.fetchall()
df = pd.read_sql_query("SELECT * FROM trades", conn )
print(df)