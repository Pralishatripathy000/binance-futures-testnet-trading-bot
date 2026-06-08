import os
import time
import hmac
import hashlib
import requests
from urllib.parse import urlencode
from dotenv import load_dotenv
from bot.logging_config import setup_logger

load_dotenv()
logger = setup_logger()


class BinanceFuturesClient:
    def __init__(self):
        self.api_key = os.getenv("BINANCE_API_KEY")
        self.api_secret = os.getenv("BINANCE_API_SECRET")
        self.base_url = "https://demo-fapi.binance.com"

        if not self.api_key or not self.api_secret:
            raise ValueError("Missing Binance API key or secret in .env file")

    def _sign(self, params):
        query_string = urlencode(params)
        return hmac.new(
            self.api_secret.encode("utf-8"),
            query_string.encode("utf-8"),
            hashlib.sha256
        ).hexdigest()

    def signed_request(self, method, endpoint, params=None):
        if params is None:
            params = {}

        params["timestamp"] = int(time.time() * 1000)
        params["signature"] = self._sign(params)

        headers = {
            "X-MBX-APIKEY": self.api_key
        }

        url = self.base_url + endpoint

        logger.info(f"API Request | {method} {url} | Params={params}")

        response = requests.request(
            method=method,
            url=url,
            headers=headers,
            params=params,
            timeout=10
        )

        logger.info(f"API Response | Status={response.status_code} | Body={response.text}")

        if response.status_code >= 400:
            raise Exception(f"API Error {response.status_code}: {response.text}")

        return response.json()

    def get_account_info(self):
        return self.signed_request("GET", "/fapi/v2/account")