import os
import sys
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

# ---------- API KEYS ----------
API_KEY = os.getenv("BINANCE_API_KEY")
API_SECRET = os.getenv("BINANCE_API_SECRET")

if not API_KEY or not API_SECRET:
    raise Exception("API KEY or API SECRET not found in environment variables")

client = Client(API_KEY, API_SECRET)
client.FUTURES_URL = "https://testnet.binancefuture.com"
# ----------------------------


def main():
    if len(sys.argv) != 6:
        print("Usage: python stop_limit.py SYMBOL SIDE QTY STOP_PRICE LIMIT_PRICE")
        return

    symbol = sys.argv[1]
    side = sys.argv[2]
    qty = float(sys.argv[3])
    stop_price = float(sys.argv[4])
    limit_price = float(sys.argv[5])

    try:
        order = client.futures_create_order(
            symbol=symbol,
            side=side,
            type="STOP",
            quantity=qty,
            stopPrice=stop_price,
            price=limit_price,
            timeInForce="GTC"
        )

        logging.info("Stop-Limit order placed: %s", order)
        print("Stop-Limit Order Placed Successfully")

    except Exception as e:
        logging.error(str(e))
        print("Error:", e)


if __name__ == "__main__":
    main()
