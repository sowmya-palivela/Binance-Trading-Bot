import argparse
import logging

from bot.client import create_client
from bot.orders import place_order
from bot.validators import validate_order
from bot.logging_config import setup_logger

# Replace with your Binance Testnet API keys
API_KEY = "API_KEY"
API_SECRET = "Secret_Key"


def main():

    setup_logger()

    parser = argparse.ArgumentParser(description="Binance Futures Trading Bot")

    parser.add_argument("--symbol", required=True, help="Trading pair (e.g., BTCUSDT)")
    parser.add_argument("--side", required=True, help="BUY or SELL")
    parser.add_argument("--type", required=True, help="MARKET or LIMIT")
    parser.add_argument("--quantity", type=float, required=True, help="Order quantity")
    parser.add_argument("--price", type=float, help="Price required for LIMIT orders")

    args = parser.parse_args()

    try:

        validate_order(args.symbol, args.side, args.type, args.quantity, args.price)

        client = create_client(API_KEY, API_SECRET)

        order = place_order(
            client,
            args.symbol,
            args.side,
            args.type,
            args.quantity,
            args.price
        )

        print("\nOrder Summary")
        print("---------------------")
        print("Order ID:", order.get("orderId"))
        print("Status:", order.get("status"))
        print("Executed Quantity:", order.get("executedQty"))

    except Exception as e:

        logging.error(f"Execution failed: {e}")
        print("Error:", e)


if __name__ == "__main__":
    main()
