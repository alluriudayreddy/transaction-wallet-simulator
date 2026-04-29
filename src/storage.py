from model import Wallet
import json

def save_wallets(wallets):
    wallets_data = {}

    for wallet_id, wallet_obj in wallets.items():
        wallets_data[wallet_id] = {
            "wallet ID": wallet_obj.wallet_id,
            "owner": wallet_obj.owner,
            "balance": wallet_obj.balance,
            "history": wallet_obj.history
        }

        with open("data/wallets.json", "w") as file:
            json.dump(wallets_data, file, indent=4)


def load_wallets():
    with open("data/wallets.json", "r") as file:
        wallets_data = json.load(file)

    wallets = {}

    for wallet_id, wallet_info in wallets_data.items():
        wallet_obj = Wallet(
            wallet_info["wallet ID"],
            wallet_info["owner"],
            wallet_info["balance"]
        )

        wallet_obj.history = wallet_info["history"]
        wallets[wallet_id] = wallet_obj

    return wallets