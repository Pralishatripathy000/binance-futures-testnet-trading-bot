import argparse
from bot.client import BinanceFuturesClient
from bot.orders import place_market_order, place_limit_order
from bot.validators import validate_side, validate_order_type, validate_quantity, validate_price


def print_order_response(response):
    print("===== ORDER RESPONSE =====")
    print(f"Order ID     : {response.get('orderId')}")
    print(f"Status       : {response.get('status')}")
    print(f"Executed Qty : {response.get('executedQty')}")
    print(f"Avg Price    : {response.get('avgPrice')}")
    print("==========================")


def main():
    parser = argparse.ArgumentParser(description="Binance Futures Testnet Trading Bot")

    parser.add_argument("--symbol", required=True)
    parser.add_argument("--side", required=True)
    parser.add_argument("--type", required=True)
    parser.add_argument("--quantity", required=True)
    parser.add_argument("--price", required=False)

    args = parser.parse_args()

    try:
        symbol = args.symbol.upper()
        side = validate_side(args.side)
        order_type = validate_order_type(args.type)
        quantity = validate_quantity(args.quantity)

        client = BinanceFuturesClient()

        if order_type == "MARKET":
            response = place_market_order(client, symbol, side, quantity)
            print_order_response(response)
            print("Market order placed successfully.")

        elif order_type == "LIMIT":
            price = validate_price(args.price)
            response = place_limit_order(client, symbol, side, quantity, price)
            print_order_response(response)
            print("Limit order placed successfully.")

    except Exception as e:
        print("Order failed.")
        print(e)


if __name__ == "__main__":
    main()