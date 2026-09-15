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