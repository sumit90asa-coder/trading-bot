# Binance Futures Trading Bot (Testnet)

## Overview

This project is a CLI-based trading bot built using Python that interacts with Binance Futures Testnet. It supports placing MARKET and LIMIT orders with proper logging and error handling.

---

## Features

* Place MARKET and LIMIT orders
* Supports BUY and SELL
* CLI-based input using Typer
* Logging of API requests and responses
* Input validation and error handling

---

## Setup

### 1. Clone the repository

```
git clone <your-repo-link>
cd trading_bot
```

### 2. Create virtual environment

```
python -m venv venv
venv\Scripts\activate
```

### 3. Install dependencies

```
pip install -r requirements.txt
```

### 4. Create .env file

```
API_KEY=your_api_key
API_SECRET=your_api_secret
```

---

## Usage

### MARKET Order

```
python cli.py --symbol BTCUSDT --side BUY --order-type MARKET --quantity 0.001
```

### LIMIT Order

```
python cli.py --symbol BTCUSDT --side SELL --order-type LIMIT --quantity 0.001 --price 60000
```

---

## Logs

All logs are stored in:

```
logs/trading.log
```

---

## Assumptions

* Using Binance Futures Testnet
* API keys are valid and have trading permissions

---

## Tech Stack

* Python
* python-binance
* Typer
* Loguru

---

## Author
Sumit Soni
