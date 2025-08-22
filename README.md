# Stock Market Dashboard

A Python project to fetch stock data using [Yahoo Finance](https://pypi.org/project/yfinance/),  
analyze it, and plot visualizations.  
Supports **single or multiple tickers** with closing price charts, basic statistics,  
and moving averages (if only one ticker is provided).

---

## Features
- Fetch historical stock data from Yahoo Finance
- Supports multiple tickers (e.g., `AAPL TSLA MSFT`)
- Displays:
  - Highest, lowest, and average closing prices
  - Line chart of stock prices
  - 7-day and 30-day moving averages (for single ticker)
- Robust input validation for dates and ticker symbols

---

## Requirements
Install dependencies using:
```bash
pip install -r requirements.txt
