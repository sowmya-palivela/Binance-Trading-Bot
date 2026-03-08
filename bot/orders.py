import logging
import random

logger = logging.getLogger()

def place_order(client, symbol, side, order_type, quantity, price=None):

    try:

        # simulate order response
        order = {
            "orderId": random.randint(1000000,9999999),
            "status": "FILLED" if order_type=="MARKET" else "NEW",
            "executedQty": quantity,
            "symbol": symbol,
            "side": side,
            "type": order_type
        }

        logger.info(f"Order response: {order}")

        print("\nFull API Response:")
        print(order)

        return order

    except Exception as e:
        logger.error(f"Error placing order: {e}")
        raise
