<p align = "center">

<img width="1983" height="793" alt="ChatGPT Image Jun 8, 2026, 09_49_01 PM" src="https://github.com/user-attachments/assets/5eac04f6-f495-490b-9bb1-c773a6c4577c" />

</p>



# Binance Futures Testnet Trading Bot

## Overview

A Python-based CLI Trading Bot for Binance Futures Demo/Testnet that supports Market and Limit order placement for USDT-M Futures contracts.

The application is designed with a modular structure, input validation, logging, and exception handling to ensure maintainability and reliability.

---

## Features

* Place MARKET orders
* Place LIMIT orders
* Supports BUY and SELL sides
* Command-line interface using argparse
* Input validation
* Structured logging
* Error handling for:

  * Invalid inputs
  * API errors
  * Network failures
* Binance Futures Demo/Testnet integration

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
│   └── logging_config.py
│
├── logs/
│   └── trading_bot.log
│
├── cli.py
├── requirements.txt
├── .env
├── .gitignore
└── README.md
```

---

## Installation

### 1. Clone Repository

```bash
git clone <repository-url>
cd trading_bot
```

### 2. Create Virtual Environment

```bash
python -m venv venv
```

Activate:

Windows

```bash
venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Environment Variables

Create a `.env` file:

```env
BINANCE_API_KEY=YOUR_API_KEY
BINANCE_API_SECRET=YOUR_API_SECRET
```

---

## Usage

### Market Buy Order

```bash
python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.001
```

### Market Sell Order

```bash
python cli.py --symbol BTCUSDT --side SELL --type MARKET --quantity 0.001
```

### Limit Buy Order

```bash
python cli.py --symbol BTCUSDT --side BUY --type LIMIT --quantity 0.001 --price 90000
```

### Limit Sell Order

```bash
python cli.py --symbol BTCUSDT --side SELL --type LIMIT --quantity 0.001 --price 150000
```

---

## Sample Output

### Market Order

```text
===== ORDER REQUEST =====

Symbol     : BTCUSDT
Side       : BUY
Order Type : MARKET
Quantity   : 0.001

===== ORDER RESPONSE =====

Order ID     : 14495634202
Status       : NEW
Executed Qty : 0.0000
Avg Price    : None

Market order placed successfully.
```

### Limit Order

```text
===== ORDER REQUEST =====

Symbol     : BTCUSDT
Side       : SELL
Order Type : LIMIT
Quantity   : 0.001
Price      : 150000

===== ORDER RESPONSE =====

Order ID     : 14497312934
Status       : NEW
Executed Qty : 0.0000
Avg Price    : None

Limit order placed successfully.
```

---

## Logging

All requests, responses, and errors are logged to:

```text
logs/trading_bot.log
```

Example:

```text
INFO | API Request
INFO | API Response
INFO | Market Order Placed
INFO | Limit Order Placed
ERROR | API Error
```

---

## Assumptions

* Binance Demo Trading / Futures Testnet account is configured.
* API keys are valid and have trading permissions.
* User has sufficient demo balance for order placement.
* USDT-M Futures contracts are used.

---
## Future Improvements

- Stop-Loss and Take-Profit Orders
- Trading Strategy Layer
- Position Monitoring
- Real-time Market Data Integration
---
## Dependencies

```text
requests
python-dotenv
```

---

## Author

Pralisha Tripathy
Python Developer Assignment Submission
