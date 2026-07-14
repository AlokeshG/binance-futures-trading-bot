import os
import time
import hmac
import hashlib
import requests
from urllib.parse import urlencode
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("API_KEY")
API_SECRET = os.getenv("API_SECRET")
BASE_URL = os.getenv("BASE_URL", "https://testnet.binancefuture.com")


class BinanceClient:

    def __init__(self):
        self.api_key = API_KEY
        self.secret = API_SECRET
        self.base_url = BASE_URL

    def _headers(self):
        return {
            "X-MBX-APIKEY": self.api_key
        }

    def _sign(self, params):
        query = urlencode(params)
        signature = hmac.new(
            self.secret.encode(),
            query.encode(),
            hashlib.sha256
        ).hexdigest()

        return query + "&signature=" + signature

    def get_account(self):

        params = {
            "timestamp": int(time.time()*1000)
        }

        query = self._sign(params)

        url = f"{self.base_url}/fapi/v2/account?{query}"

        response = requests.get(
            url,
            headers=self._headers()
        )

        return response.status_code, response.json()