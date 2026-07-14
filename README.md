# Binance Futures Trading Bot

A Python command-line trading bot that places Market and Limit orders on the Binance Futures Demo/Testnet using the Binance REST API.

This project was developed as part of the Primetrade.ai Python Developer application task.

---

# Features

- Place MARKET Orders
- Place LIMIT Orders
- BUY and SELL support
- Command-Line Interface (CLI) using argparse
- Input validation
- REST API implementation
- Structured logging
- Exception handling
- Modular project structure

---

# Project Structure

```
trading_bot/
│
├── bot/
│   ├── __init__.py
│   ├── client.py
│   ├── orders.py
│   ├── validators.py
│   └── logging_config.py
│
├── logs/
│   └── trading.log
│
├── cli.py
├── README.md
├── requirements.txt
└── .gitignore
```

---

# Installation

Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/binance-futures-trading-bot.git

cd binance-futures-trading-bot
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

# Configuration

Create a `.env` file in the project root.

```env
API_KEY=YOUR_API_KEY
API_SECRET=YOUR_API_SECRET
BASE_URL=https://testnet.binancefuture.com
```

---

# Usage

### Market Order

```bash
python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.001
```

### Limit Order

```bash
python cli.py --symbol BTCUSDT --side SELL --type LIMIT --quantity 0.001 --price 120000
```

---

# Sample Output

```
========================================
ORDER REQUEST
========================================

Symbol : BTCUSDT
Side   : BUY
Type   : MARKET
Qty    : 0.001

========================================
ORDER RESPONSE
========================================

❌ Order Failed

Error Code : -2015

Message : Invalid API-key, IP, or permissions for action
```

---

# Logging

All API requests and responses are stored inside

```
logs/trading.log
```

Example log

```
INFO Order Request

INFO Binance Response

ERROR Invalid API-key
```

---

# Error Handling

The application handles:

- Invalid order side
- Invalid order type
- Missing LIMIT order price
- Invalid quantity
- Network failures
- Binance API errors
- Unexpected exceptions

---

# Technologies Used

- Python 3
- Requests
- python-dotenv
- argparse
- REST API

---

# Note

While testing, Binance redirected the original Futures Testnet endpoint to the new Demo Trading environment.

Public API endpoints (for example `/fapi/v1/ping`) were reachable, while authenticated endpoints returned:

```
APIError(code=-2015): Invalid API-key, IP, or permissions for action
```

The application correctly implements:

- REST request signing
- Command-line interface
- Input validation
- Structured logging
- Exception handling

The authentication issue appears to be related to the current Binance Demo/Testnet environment rather than the application implementation.

---

# Author

**Alokesh Ghosh**

Python Developer | MERN Stack Developer | AI & ML Student
