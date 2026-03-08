# Binance Futures Trading Bot (Testnet)

A modular Python CLI trading bot that places MARKET and LIMIT orders on Binance Futures Testnet with structured logging and input validation.

## Setup

Install dependencies:

pip install -r requirements.txt

## Run the Bot

### MARKET Order

python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.001

### LIMIT Order

python cli.py --symbol BTCUSDT --side BUY --type LIMIT --quantity 0.001 --price 60000

## Logging

All API responses and errors are logged in:

trading_bot.log

## Notes


This project demonstrates trading bot architecture and order placement workflow for Binance Futures Testnet.
