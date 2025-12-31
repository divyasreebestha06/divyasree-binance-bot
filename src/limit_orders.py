import os
import sys
import logging
from binance.client import Client

# ---------- LOGGING ----------
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LOG_DIR = os.path.join(BASE_DIR, "logs")
os.makedirs(LOG_DIR, exist_ok=True)

logging.basicConfig(
    filename=os.path.join(LOG_DIR, "bot.log"),
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)
# ----------------------------

def validate_args(args):
    if len(args) != 5:
        print("Usage: python limit_orders.py SYMBOL SIDE QTY PRICE")
        sys.exit(1)

    symbol = args[1].upper()
    side = args[2].upper()
    qty = float(args[3])
    price = float(args[4])

    if side not in ["BUY", "SELL"]:
        raise ValueError("Side must be BUY or SELL")
    if qty <= 0 or price <= 0:
        raise ValueError("Quantity and Price must be > 0")

    return symbol, side, qty, price


def main():
    try:
        # ✅ READ FROM ENVIRONMENT
        api_key = os.getenv("BINANCE_API_KEY")
        api_secret = os.getenv("BINANCE_API_SECRET")

        if not api_key or not api_secret:
            raise Exception("API KEY or API SECRET not found in environment variables")

        client = Client(api_key, api_secret)
        client.FUTURES_URL = "https://testnet.binancefuture.com"

        symbol, side, qty, price = validate_args(sys.argv)

        order = client.futures_create_order(
            symbol=symbol,
            side=side,
            type="LIMIT",
            timeInForce="GTC",
            quantity=qty,
            price=price
        )

        logging.info("Limit order placed: %s", order)
        print("Limit Order Placed Successfully!")
        print(order)

    except Exception as e:
        logging.error(str(e))
        print("Error:", e)


if __name__ == "__main__":
    main()
