from model import WalletAccount
import json
import os

PROJECT_ROOT = os.path.dirname(os.path.dirname(__file__))
DATA_FILE = os.path.join(PROJECT_ROOT, "data", "wallets.json")


def detect_duplicate_keys(pairs):
    data = {}
    for key, value in pairs:
        if key in data:
            print(f"Warning: duplicate JSON key {key} found. Later value overwrote earlier value.")
        data[key] = value
    return data


def save_wallets(all_wallets):
    if not isinstance(all_wallets, dict):
        raise TypeError("save_wallets expected all_wallets to be a dictionary")

    wallets_data = {}
    seen_wallet_ids = set()

    for wallet_id, wallet_account in all_wallets.items():
        if wallet_id != wallet_account.wallet_id:
            print(
                f"Warning: dictionary key {wallet_id} does not match "
                f"wallet object ID {wallet_account.wallet_id}. Using key {wallet_id}."
            )

        if wallet_account.wallet_id in seen_wallet_ids:
            print(f"Warning: duplicate wallet object ID {wallet_account.wallet_id} before save.")
        seen_wallet_ids.add(wallet_account.wallet_id)

        wallets_data[wallet_id] = {
            "wallet_id": wallet_account.wallet_id,
            "owner": wallet_account.owner,
            "balance": wallet_account.balance,
            "history": wallet_account.history
        }

    os.makedirs(os.path.dirname(DATA_FILE), exist_ok=True)

    with open(DATA_FILE, "w") as file:
        json.dump(wallets_data, file, indent=4)

    print(f"Saved {len(wallets_data)} wallet(s) to {DATA_FILE}.")


def load_wallets():
    if not os.path.exists(DATA_FILE):
        print(f"No wallet file found at {DATA_FILE}. Starting with 0 wallets.")
        return {}

    try:
        with open(DATA_FILE, "r") as file:
            wallets_data = json.load(file, object_pairs_hook=detect_duplicate_keys)

        if not isinstance(wallets_data, dict):
            print(f"Error loading wallets: {DATA_FILE} must contain a JSON object.")
            return {}

        all_wallets = {}

        for wallet_id, wallet_data in wallets_data.items():
            if wallet_id in all_wallets:
                print(f"Warning: duplicate wallet ID {wallet_id} found while loading.")

            wallet_account = WalletAccount(
                wallet_data["wallet_id"],
                wallet_data["owner"],
                wallet_data["balance"]
            )

            if wallet_id != wallet_account.wallet_id:
                print(
                    f"Warning: JSON key {wallet_id} does not match "
                    f"stored wallet_id {wallet_account.wallet_id}."
                )

            wallet_account.history = wallet_data.get("history", [])
            all_wallets[wallet_id] = wallet_account

        print(f"Loaded {len(all_wallets)} wallet(s) from {DATA_FILE}.")
        return all_wallets

    except (json.JSONDecodeError, KeyError, TypeError) as error:
        print(f"Error loading wallets: {error}")
        return {}
