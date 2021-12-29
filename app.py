import streamlit as st
import yfinance as yf

st.title("Basic Stock Price App")
st.write("### Welcome! Please select a company you want to view the stock price of :)")
st.text("")
c1, c2, c3, c4, c5 = st.beta_columns(5)
if c1.button("Google"):
    ticker = "GOOGL"
    google_ticker = yf.Ticker(ticker)
    google_tickerdf = google_ticker.history(period = '5y',  interval = '1d')

    st.line_chart(google_tickerdf.Close)
    st.line_chart(google_tickerdf.Volume)

if c2.button("Coinbase"):
    ticker = "COIN"
    coin_ticker = yf.Ticker(ticker)
    coin_tickerdf = coin_ticker.history(period = '5y',  interval = '1d')

    st.line_chart(coin_tickerdf.Close)
    st.line_chart(coin_tickerdf.Volume)

if c3.button("Robinhood"):
    ticker = "HOOD"
    hood_ticker = yf.Ticker(ticker)
    hood_tickerdf = hood_ticker.history(period = '5y',  interval = '1d')

    st.line_chart(hood_tickerdf.Close)
    st.line_chart(hood_tickerdf.Volume)

if c4.button("AMC"):
    ticker = "AMC"
    amc_ticker = yf.Ticker(ticker)
    amc_tickerdf = amc_ticker.history(period = '5y',  interval = '1d')

    st.line_chart(amc_tickerdf.Close)
    st.line_chart(amc_tickerdf.Volume)
    
if c5.button("Walt Disney"):
    ticker = "DIS"
    dis_ticker = yf.Ticker(ticker)
    dis_tickerdf = dis_ticker.history(period = '5y',  interval = '1d')

    st.line_chart(dis_tickerdf.Close)
    st.line_chart(dis_tickerdf.Volume)
    

backgroundColor = '#273346'