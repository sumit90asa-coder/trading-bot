from binance.client import Client
from dotenv import load_dotenv
import os

load_dotenv()

class BinanceClient:
    def __init__(self):
        self.client = Client(
            os.getenv("API_KEY"),
            os.getenv("API_SECRET"),
            testnet=True   # ✅ THIS IS THE FIX
        )

    def place_order(self, **params):
        return self.client.futures_create_order(**params)