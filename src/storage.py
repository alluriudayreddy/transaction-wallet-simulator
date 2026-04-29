from model import WalletAccount
import json


def save_wallets(all_wallets):
    wallets_data = {}

    for wallet_id, wallet_account in all_wallets.items():
        wallets_data[wallet_id] = {
            "wallet_id": wallet_account.wallet_id,
            "owner": wallet_account.owner,
            "balance": wallet_account.balance,
            "history": wallet_account.history
        }

    with open("data/wallets.json", "w") as file:
        json.dump(wallets_data, file, indent=4)


def load_wallets():
    with open("data/wallets.json", "r") as file:
        wallets_data = json.load(file)

    all_wallets = {}

    for wallet_id, wallet_data in wallets_data.items():
        wallet_account = WalletAccount(
            wallet_data["wallet_id"],
            wallet_data["owner"],
            wallet_data["balance"]
        )

        wallet_account.history = wallet_data["history"]
        all_wallets[wallet_id] = wallet_account

    return all_wallets