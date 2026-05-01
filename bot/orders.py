from bot.client import BinanceClient
from loguru import logger

client = BinanceClient()

def execute_order(symbol, side, order_type, quantity, price=None):
    try:
        params = {
            "symbol": symbol,
            "side": side,
            "type": order_type,
            "quantity": quantity,
        }

        if order_type == "LIMIT":
            params["price"] = price
            params["timeInForce"] = "GTC"

        logger.info(f"Placing order: {params}")

        response = client.place_order(**params)

        logger.info(f"Response: {response}")

        return response

    except Exception as e:
        logger.error(f"Error placing order: {str(e)}")
        raise