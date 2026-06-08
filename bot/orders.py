from bot.logging_config import setup_logger

logger = setup_logger()


def print_order_summary(symbol, side, order_type, quantity, price=None):
    print("\n===== ORDER REQUEST =====")
    print(f"Symbol     : {symbol}")
    print(f"Side       : {side}")
    print(f"Order Type : {order_type}")
    print(f"Quantity   : {quantity}")

    if price:
        print(f"Price      : {price}")

    print("=========================\n")

    logger.info(
        f"Order Request | Symbol={symbol} Side={side} Type={order_type} Quantity={quantity} Price={price}"
    )


def place_market_order(client, symbol, side, quantity):
    params = {
        "symbol": symbol,
        "side": side,
        "type": "MARKET",
        "quantity": quantity
    }

    print_order_summary(symbol, side, "MARKET", quantity)

    response = client.signed_request("POST", "/fapi/v1/order", params)

    logger.info(f"Market Order Placed | Response={response}")

    return response


def place_limit_order(client, symbol, side, quantity, price):
    params = {
        "symbol": symbol,
        "side": side,
        "type": "LIMIT",
        "quantity": quantity,
        "price": price,
        "timeInForce": "GTC"
    }

    print_order_summary(symbol, side, "LIMIT", quantity, price)

    response = client.signed_request("POST", "/fapi/v1/order", params)

    logger.info(f"Limit Order Placed | Response={response}")

    return response