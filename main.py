# stock_dashboard.py
# Stock Market Dashboard: Fetches stock data using Yahoo Finance,
# shows statistics, and plots prices (supports one or multiple tickers).

import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

def validate_date(date_str):
    """Check if the date is in YYYY-MM-DD format."""
    try:
        datetime.strptime(date_str, "%Y-%m-%d")
        return True
    except ValueError:
        return False

def stock_analysis(tickers, start_date, end_date):
    # Fetch stock data for one or multiple tickers
    data = yf.download(tickers, start=start_date, end=end_date)

    # Get only closing prices
    close_data = data['Close']

    # If single ticker, convert Series → DataFrame for consistency
    if isinstance(close_data, pd.Series):
        close_data = close_data.to_frame(name=tickers[0])

    # Print statistics for each ticker
    for ticker in close_data.columns:
        highest = close_data[ticker].max()
        lowest = close_data[ticker].min()
        average = close_data[ticker].mean()
        print(f"\nStock: {ticker}")
        print(f"Date Range: {start_date} to {end_date}")
        print(f"Highest Closing Price: {highest:.2f}")
        print(f"Lowest Closing Price: {lowest:.2f}")
        print(f"Average Closing Price: {average:.2f}")

    # Plot all tickers on one chart
    plt.figure(figsize=(12,6))
    for ticker in close_data.columns:
        plt.plot(close_data[ticker], label=f"{ticker} Closing Price")
    plt.title("Stock Prices")
    plt.xlabel("Date")
    plt.ylabel("Price")
    plt.legend()
    plt.grid(True)
    plt.show()

    # If only one ticker, also show moving averages
    if len(close_data.columns) == 1:
        ticker = close_data.columns[0]
        df = close_data.copy()
        df['7-day MA'] = df[ticker].rolling(window=7).mean()
        df['30-day MA'] = df[ticker].rolling(window=30).mean()

        plt.figure(figsize=(12,6))
        plt.plot(df[ticker], label='Closing Price')
        plt.plot(df['7-day MA'], label='7-day MA')
        plt.plot(df['30-day MA'], label='30-day MA')
        plt.title(f"{ticker} Stock Price with Moving Averages")
        plt.xlabel("Date")
        plt.ylabel("Price")
        plt.legend()
        plt.grid(True)
        plt.show()

if __name__ == "__main__":
    tickers = input("Enter stock ticker(s) (e.g. AAPL TSLA RELIANCE.NS): ").upper().split()
    start_date = input("Enter start date (YYYY-MM-DD): ")
    end_date = input("Enter end date (YYYY-MM-DD): ")

    # Basic input validation
    if not tickers:
        print("Error: Please enter at least one ticker symbol.")
    elif not validate_date(start_date) or not validate_date(end_date):
        print("Error: Please enter dates in YYYY-MM-DD format.")
    else:
        stock_analysis(tickers, start_date, end_date)
