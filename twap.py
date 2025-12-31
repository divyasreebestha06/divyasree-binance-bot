import os
import sys
import time
import logging
from binance.client import Client

# ---------- LOGGING ----------
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
LOG_DIR = os.path.join(BASE_DIR, "logs")
os.makedirs(LOG_DIR, exist_ok=True)

logging.basicConfig(
    filename=os.path.join(LOG_DIR, "bot.log"),
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)
# ----------------------------

API_KEY = os.getenv("BINANCE_API_KEY")
API_SECRET = os.getenv("BINANCE_API_SECRET")

if not API_KEY or not API_SECRET:
    raise Exception("API KEY or API SECRET not found")

client = Client(API_KEY, API_SECRET)
client.FUTURES_URL = "https://testnet.binancefuture.com"


def main():
    if len(sys.argv) != 6:
        print("Usage: python twap.py SYMBOL SIDE TOTAL_QTY PARTS DELAY")
        return

    symbol = sys.argv[1]
    side = sys.argv[2]
    total_qty = float(sys.argv[3])
    parts = int(sys.argv[4])
    delay = int(sys.argv[5])

    qty_per_order = round(total_qty / parts, 6)

    print(f"Placing TWAP: {parts} orders of {qty_per_order}")

    for i in range(parts):
        order = client.futures_create_order(
            symbol=symbol,
            side=side,
            type="MARKET",
            quantity=qty_per_order
        )

        logging.info("TWAP order %d placed: %s", i + 1, order)
        print(f"Order {i + 1} placed")

        time.sleep(delay)

    print("TWAP execution completed")


if __name__ == "__main__":
    main()
