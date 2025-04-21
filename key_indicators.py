import yfinance as yf
import pandas as pd
import numpy as np

# Function to calculate RSI
def compute_rsi(data, window=14):
    delta = data.diff()
    gain = delta.where(delta > 0, 0)
    loss = -delta.where(delta < 0, 0)

    avg_gain = gain.rolling(window=window, min_periods=1).mean()
    avg_loss = loss.rolling(window=window, min_periods=1).mean()

    rs = avg_gain / avg_loss
    rsi = 100 - (100 / (1 + rs))
    return rsi

# Function to calculate MACD
def compute_macd(data):
    exp12 = data.ewm(span=12, adjust=False).mean()  # 12-period EMA
    exp26 = data.ewm(span=26, adjust=False).mean()  # 26-period EMA
    macd = exp12 - exp26
    signal = macd.ewm(span=9, adjust=False).mean()  # Signal line
    return macd, signal

# Define the tickers for the companies
tickers = ['NVDA', 'AMD', 'INTC']

# Get price data
data = {}
for ticker in tickers:
    stock = yf.Ticker(ticker)
    stock_data = stock.history(period="1y")  # Get data for the last 1 year
    stock_data['RSI'] = compute_rsi(stock_data['Close'])  # RSI Calculation
    stock_data['MACD'], stock_data['MACD_signal'] = compute_macd(stock_data['Close'])  # MACD Calculation
    stock_data['SMA_50'] = stock_data['Close'].rolling(window=50).mean()  # 50-period moving average
    stock_data['SMA_200'] = stock_data['Close'].rolling(window=200).mean()  # 200-period moving average
    data[ticker] = stock_data[['Close', 'RSI', 'MACD', 'MACD_signal', 'SMA_50', 'SMA_200']]  # Save relevant data

# Print the data for each company
for ticker in tickers:
    print(f"\n{ticker} Technical Indicators:")
    print(data[ticker].tail())  # Display the latest data for each company
