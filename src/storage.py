from model import Wallet
import json

def save_wallets(wallets):
    data = {}

    for wallet_id, wallet in wallets.items():
        data[wallet_id] = {
            "wallet_id": wallet.wallet_id,
            "owner": wallet.owner,
            "balance": wallet.balance,
            "history": wallet.history
        }

    with open("data/wallets.json", "w") as file:
        json.dump(data, file, indent=4)


def load_wallets():
    with open("data/wallets.json", "r") as file:
        data = json.load(file)

    wallets = {}

    for wallet_id, info in data.items():
        wallet = Wallet(
            info["wallet_id"],
            info["owner"],
            info["balance"]
        )

        wallet.history = info["history"]
        wallets[wallet_id] = wallet

    return wallets