import argparse

from bot.orders import place_order
from bot.validators import validate_order

parser = argparse.ArgumentParser(description="Binance Futures Trading Bot")

parser.add_argument("--symbol", required=True)
parser.add_argument("--side", required=True)
parser.add_argument("--type", required=True)
parser.add_argument("--quantity", type=float, required=True)
parser.add_argument("--price", type=float)

args = parser.parse_args()

try:
    validate_order(
        args.symbol,
        args.side,
        args.type,
        args.quantity,
        args.price
    )

    print("=" * 40)
    print("ORDER REQUEST")
    print("=" * 40)

    print(f"Symbol : {args.symbol}")
    print(f"Side   : {args.side}")
    print(f"Type   : {args.type}")
    print(f"Qty    : {args.quantity}")

    if args.price:
        print(f"Price  : {args.price}")

    response = place_order(
        args.symbol,
        args.side,
        args.type,
        args.quantity,
        args.price
    )

    print("\n" + "=" * 40)
    print("ORDER RESPONSE")
    print("=" * 40)

    if "code" in response and response["code"] < 0:
        print("❌ Order Failed")
        print("Error Code :", response["code"])
        print("Message    :", response["msg"])
    else:
        print("✅ Order Successful")
        print("Order ID     :", response.get("orderId"))
        print("Status       :", response.get("status"))
        print("Executed Qty :", response.get("executedQty"))
        print("Avg Price    :", response.get("avgPrice"))

except Exception as e:
    print("\n❌ ERROR")
    print(e)