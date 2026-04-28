from model import Wallet
import json
import os

DATA_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'data'))
DATA_FILE = os.path.join(DATA_DIR, 'wallets.json')


def save_wallet(wallet):
    os.makedirs(DATA_DIR, exist_ok=True)
    data = {
        "wallet_id": wallet.wallet_id,
        "owner": wallet.owner,
        "balance": wallet.balance,
        "history": wallet.history,
    }

    with open(DATA_FILE, "w") as file:
        json.dump(data, file, indent=4)


def load_wallet():
    if not os.path.exists(DATA_FILE):
        print(f"No saved wallet found at {DATA_FILE}.")
        return None

    with open(DATA_FILE, "r") as file:
        data = json.load(file)

    wallet = Wallet(
        data["wallet_id"],
        data["owner"],
        data["balance"],
    )
    wallet.history = data.get("history", [])
    return wallet
