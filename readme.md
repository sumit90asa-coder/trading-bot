# ** Binance Futures Trading Bot (Testnet)**

## Overview

This project is a command-line based trading bot built using Python. It connects to the Binance Futures Testnet and allows users to place market and limit orders. The application is designed with a modular structure and includes input validation, logging, and error handling.

---

## Features

* Supports market and limit orders
* Allows both buy and sell operations
* Command-line interface using Typer
* Logging of requests and responses
* Input validation and error handling
* Clean and maintainable project structure

---

## Project Structure

```text
trading_bot/
│
├── bot/
│   ├── __init__.py
│   ├── client.py
│   ├── orders.py
│   ├── validators.py
│   ├── logging_config.py
│
├── cli.py
├── requirements.txt
├── README.md
├── .env   (not included in repository)
```

---

## Installation

```bash
git clone https://github.com/YOUR_USERNAME/trading-bot.git
cd trading-bot

python -m venv venv
venv\Scripts\activate

pip install -r requirements.txt
```

---

## Environment Setup

Create a `.env` file in the root directory:

```env
API_KEY=your_api_key
API_SECRET=your_api_secret
```

---

## Usage

### Market Order

```bash
python cli.py --symbol BTCUSDT --side BUY --order-type MARKET --quantity 0.001
```

### Limit Order

```bash
python cli.py --symbol BTCUSDT --side BUY --order-type LIMIT --quantity 0.001 --price 70000
```

---

## Example Output

```text
Order Summary
Symbol: BTCUSDT
Side: BUY
Type: MARKET
Quantity: 0.001

ORDER SUCCESS
Order ID: 13095787728
Status: NEW
Executed Qty: 0.0000
```

---

## Order Rules

* For a buy limit order, the price must be lower than the current market price
* For a sell limit order, the price must be higher than the current market price

---

## Logs

All logs are stored in the following file:

```text
logs/trading.log
```

To open the log file on Windows:

```bash
notepad logs\trading.log
```

---

## Technologies Used

* Python
* python-binance
* Typer
* Loguru

---

## Notes

* This project uses the Binance Futures Testnet environment
* API keys must have appropriate trading permissions
* The `.env` file should not be committed to the repository

---

## Author

Sumit Soni

---
