from trading_journal import TradingJournal   
from fastapi import FastAPI
import sqlite3
import pandas as pd 
from pydantic import BaseModel
class Trade(BaseModel):
    open_time: str
    profit: float
app = FastAPI()
@app.get("/trades")
async def read_trades():
          conn = sqlite3.connect("trading_journal.db")
          df = pd.read_sql_query("SELECT * FROM trades", conn)
          conn.close()
          df = df.astype(object).where(pd.notnull(df), None)
          return df.to_dict(orient="records")
@app.post("/trades")    
async def log_trade(trade: Trade):
    conn = sqlite3.connect("trading_journal.db")
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO trades (open_time, profit) VALUES (?, ?)",
        (trade.open_time, trade.profit),
    )
    conn.commit()
    conn.close()
    return {"message": "Trade logged successfully."}
@app.delete("/trades")
async def delete_trades (rowid: int):
    conn = sqlite3.connect("trading_journal.db")
    cursor = conn.cursor()
    cursor.execute("DELETE FROM trades WHERE rowid = ?", (rowid,))  
    conn.commit()
    conn.close()
    return {"message": "Trade deleted successfully."}  
@app.get("/stats")
async def get_stats():
    conn = sqlite3.connect("trading_journal.db")
    df = pd.read_sql_query("SELECT * FROM trades", conn)
    conn.close()

    journal = TradingJournal(df)    
    journal.calculate_all_stats()          

    return {
        "win_rate": journal.win_rate,
        "profit_factor": None if journal.profit_factor == float('inf') else journal.profit_factor,
        "expectancy": journal.expectancy,
        "drawdown": journal.drawdown,
        "session_stats": journal.session_stats.to_dict() if journal.session_stats is not None else None,
        "best_trade": journal.best_trade.to_dict() if journal.best_trade is not None else None,
        "worst_trade": journal.worst_trade.to_dict() if journal.worst_trade is not None else None   
    }