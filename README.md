Binance Futures Trading Bot (Testnet)
📌 Project Overview

This project is a Python-based Binance Futures Trading Bot built using the Binance Futures Testnet.
It allows users to place different types of futures orders via a command-line interface (CLI) and demonstrates both basic and advanced order execution strategies.

The project is developed as part of a Python internship / assignment to showcase:

API integration

Order management

Logging

Advanced trading strategies

🚀 Features
✅ Basic Orders

Market Order

Limit Order

✅ Advanced Orders

Stop-Limit Order

OCO Order (Simulated for Futures)

TWAP (Time-Weighted Average Price) Strategy

✅ Other Features

Binance Futures Testnet integration

Command-line based execution

Centralized logging (bot.log)

Clean modular project structure

📁 Project Structure
divyasree_binance_bot/
│
├── src/
│   ├── market_orders.py        # Market order execution
│   ├── limit_orders.py         # Limit order execution
│   │
│   └── advanced/
│       ├── stop_limit.py       # Stop-Limit order
│       ├── oco.py              # Simulated OCO order
│       └── twap.py             # TWAP strategy
│
├── logs/
│   └── bot.log                 # Order & error logs
│
├── README.md                   # Project documentation

🔑 Environment Setup
1️⃣ Install Dependencies
pip install python-binance

2️⃣ Set Binance Testnet API Keys (Windows CMD)
set BINANCE_API_KEY=YOUR_TESTNET_API_KEY
set BINANCE_API_SECRET=YOUR_TESTNET_API_SECRET


⚠️ Do NOT hardcode API keys inside Python files

▶️ How to Run the Bot

Run all commands from the project root folder:

divyasree_binance_bot

🟢 Market Order
python src/market_orders.py BTCUSDT BUY 0.001

🟡 Limit Order
python src/limit_orders.py BTCUSDT BUY 0.001 88000

🔵 Stop-Limit Order
python src/advanced/stop_limit.py BTCUSDT SELL 0.001 90000 89500

🔴 OCO Order (Simulated)

Binance Futures does not support classic OCO, so this is simulated using two orders.

python src/advanced/oco.py BTCUSDT SELL 0.001 90000 87000 86500

🟣 TWAP Strategy

Splits a large order into smaller market orders over time.

python src/advanced/twap.py BTCUSDT BUY 0.005 5 5


Explanation:

Total quantity: 0.005

Split into: 5 orders

Interval: 5 seconds

📝 Logging

All orders and errors are logged automatically in:

logs/bot.log


This helps in tracking executions and debugging issues.

⚠️ Disclaimer

This bot is designed only for educational purposes and uses Binance Testnet.
It should not be used for real trading without proper risk management and testing.
