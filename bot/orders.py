import time
import requests
import hmac
import hashlib
from urllib.parse import urlencode
from dotenv import load_dotenv
import os

from bot.logging_config import setup_logger

logger = setup_logger()

load_dotenv()

BASE_URL = os.getenv("BASE_URL")
API_KEY = os.getenv("API_KEY")
API_SECRET = os.getenv("API_SECRET")


def sign(params):
    query = urlencode(params)
    signature = hmac.new(
        API_SECRET.encode(),
        query.encode(),
        hashlib.sha256
    ).hexdigest()

    return query + "&signature=" + signature


def place_order(symbol, side, order_type, quantity, price=None):

    params = {
        "symbol": symbol.upper(),
        "side": side.upper(),
        "type": order_type.upper(),
        "quantity": quantity,
        "timestamp": int(time.time() * 1000)
    }

    if order_type.upper() == "LIMIT":
        params["price"] = price
        params["timeInForce"] = "GTC"

    query = sign(params)

    url = BASE_URL + "/fapi/v1/order?" + query

    headers = {
        "X-MBX-APIKEY": API_KEY
    }

    logger.info(f"Order Request: {params}")

    try:
        response = requests.post(url, headers=headers)

        logger.info(f"Response: {response.text}")

        return response.json()

    except Exception as e:
        logger.error(str(e))
        return {"error": str(e)}