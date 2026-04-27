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