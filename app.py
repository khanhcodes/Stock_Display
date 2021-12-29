import streamlit as st
from streamlit import config
import yfinance as yf
import pandas as pd

st.title("Basic Stock Price App")
st.write("##### Welcome! Please select a company you want to view the stock prices of. All the data is up-to-date :)")
st.text("")
c1, c2, c3, c4, c5 = st.columns(5)

def remove_unnecessary_column(df):
    df.pop("Dividends")
    df.pop("Stock Splits")

if c1.button("Google"):
    ticker = "GOOGL"
    google_ticker = yf.Ticker(ticker)
    google_tickerdf = google_ticker.history(period = '5y',  interval = '1d')
    st.write("#### Closing Price")
    st.line_chart(google_tickerdf.Close)
    st.write("#### Volume Price")
    st.line_chart(google_tickerdf.Volume)
    remove_unnecessary_column(google_tickerdf)
    
    st.caption("Stock prices in table")
    st.write(google_tickerdf)



if c2.button("Coinbase"):
    ticker = "COIN"
    coin_ticker = yf.Ticker(ticker)
    coin_tickerdf = coin_ticker.history(period = '5y',  interval = '1d')
    st.write("#### Closing Price")
    st.line_chart(coin_tickerdf.Close)
    st.write("#### Volume Price")
    st.line_chart(coin_tickerdf.Volume)
    remove_unnecessary_column(coin_tickerdf)
    
    st.caption("Stock prices in table")
    st.write(coin_tickerdf)

if c3.button("Robinhood"):
    ticker = "HOOD"
    hood_ticker = yf.Ticker(ticker)
    hood_tickerdf = hood_ticker.history(period = '5y',  interval = '1d')
    st.write("#### Closing Price")
    st.line_chart(hood_tickerdf.Close)
    st.write("#### Volume Price")
    st.line_chart(hood_tickerdf.Volume)
    remove_unnecessary_column(hood_tickerdf)
    
    st.caption("Stock prices in table")
    st.write(hood_tickerdf)

if c4.button("AMC"):
    ticker = "AMC"
    amc_ticker = yf.Ticker(ticker)
    amc_tickerdf = amc_ticker.history(period = '5y',  interval = '1d')
    st.write("#### Closing Price")
    st.line_chart(amc_tickerdf.Close)
    st.write("#### Volume Price")
    st.line_chart(amc_tickerdf.Volume)
    remove_unnecessary_column(amc_tickerdf)
    
    st.caption("Stock prices in table")
    st.write(amc_tickerdf)
    
if c5.button("Walt Disney"):
    ticker = "DIS"
    dis_ticker = yf.Ticker(ticker)
    dis_tickerdf = dis_ticker.history(period = '5y',  interval = '1d')
    st.write("#### Closing Price")
    st.line_chart(dis_tickerdf.Close)
    st.write("#### Volume Price")
    st.line_chart(dis_tickerdf.Volume)
    remove_unnecessary_column(dis_tickerdf)
    
    st.caption("Stock prices in table")
    st.write(dis_tickerdf)
