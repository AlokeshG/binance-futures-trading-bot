VALID_SIDES = ["BUY", "SELL"]
VALID_TYPES = ["MARKET", "LIMIT"]


def validate_order(symbol, side, order_type, quantity, price=None):
    if not symbol:
        raise ValueError("Symbol cannot be empty.")

    side = side.upper()
    order_type = order_type.upper()

    if side not in VALID_SIDES:
        raise ValueError("Side must be BUY or SELL.")

    if order_type not in VALID_TYPES:
        raise ValueError("Order type must be MARKET or LIMIT.")

    if quantity <= 0:
        raise ValueError("Quantity must be greater than 0.")

    if order_type == "LIMIT":
        if price is None:
            raise ValueError("Price is required for LIMIT orders.")
        if price <= 0:
            raise ValueError("Price must be greater than 0.")

    return True