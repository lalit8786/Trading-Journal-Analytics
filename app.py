import streamlit as st
import pandas as pd
import sqlite3
from trading_journal import TradingJournal

st.set_page_config(page_title="Trading Journal Dashboard", layout="wide")
@st.cache_data
def load_data(): 
 conn=sqlite3.connect("trading_journal.db") 
 cursor= conn.cursor()
 df = pd.read_sql_query("SELECT * FROM trades", conn)
 conn.close()
 return df

if "journal" not in st.session_state:
    df = load_data()
    st.session_state.journal = TradingJournal(df)
    st.session_state.journal.calculate_all_stats()

journal = st.session_state.journal

st.title("Trading Journal Dashboard")
col1, col2, col3, col4 = st.columns(4)
col1.metric("Win Rate", f"{journal.win_rate:.2f}%")
col2.metric("Profit Factor", f"{journal.profit_factor:.2f}")
col3.metric("Expectancy", f"{journal.expectancy:.2f}")
col4.metric("Drawdown", f"{journal.drawdown:.2f}")

st.divider()
st.subheader("Average Profit by Session")
st.bar_chart(journal.session_stats)

st.divider()
st.subheader("All Trades")
st.dataframe(journal.df, use_container_width=True)

st.divider()
st.subheader("Equity Curve")
st.line_chart(journal.running_balance)

st.subheader("Log a New Trade")
with st.form("log_trade_form", clear_on_submit=True):
    open_time = st.text_input("Open Time (YYYY-MM-DD HH:MM:SS)")
    profit = st.number_input("Profit", step=0.01, format="%.2f")
    submitted = st.form_submit_button("Log Trade")

    if submitted:
        if open_time.strip() == "":
            st.error("Please enter an open time.")
        else:
            trade_dict = {"open_time": open_time, "profit": profit}
            journal.log_trades(trade_dict)
            conn = sqlite3.connect("trading_journal.db")
            cursor = conn.cursor()
            cursor.execute("INSERT INTO trades (open_time, profit) VALUES (?, ?)", (open_time, profit))
            conn.commit()
            conn.close()
            st.success("Trade logged! Stats refreshed below.")
            st.rerun()
if st.button("Undo Last Trade"):
    journal.undo_last_trade()
    conn = sqlite3.connect("trading_journal.db")
    cursor = conn.cursor()
    cursor.execute("DELETE FROM trades WHERE rowid = (SELECT MAX(rowid) FROM trades)")
    conn.commit()
    conn.close()
    st.success("Last trade undone.")
    st.rerun()
