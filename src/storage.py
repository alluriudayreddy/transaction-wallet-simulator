from model import Wallet
import json

def save_wallet(wallet):
    data={
        "wallet_id": wallet.wallet_id,
        "owner": wallet.owner,
        "balance": wallet.balance,
        "history": wallet.history
    }

    with open("data/wallets.json", "w") as file:
        json.dump(data, file, indent=4)



def load_wallet():
    with open("data/wallets.json", "r") as file:
        data = json.load(file)

    wallet = Wallet(
        data["wallet_id"],
        data["owner"],
        data["balance"]
    )

    wallet.history = data["history"]
    return wallet