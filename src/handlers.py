from model import WalletAccount
from operations import deposit, withdraw, transfer
from storage import save_wallets, load_wallets
from helpers import generate_wallet_id, show_wallet, show_history, show_all_wallets


def handle_create_wallet(all_wallets):
    owner_name = input("Enter owner name: ")
    wallet_id = generate_wallet_id()

    all_wallets[wallet_id] = WalletAccount(wallet_id, owner_name, 0)
    print(f"Wallet created with ID: {wallet_id}")


def handle_deposit(all_wallets):
    wallet_id = input("Enter wallet ID: ")

    if wallet_id in all_wallets:
        amount = float(input("Enter amount: "))
        try:
            deposit(all_wallets[wallet_id], amount)
            print("Deposit successful")
        except ValueError as error:
            print(error)
    else:
        print("Wallet ID not found")


def handle_withdraw(all_wallets):
    wallet_id = input("Enter wallet ID: ")

    if wallet_id in all_wallets:
        amount = float(input("Enter amount: "))
        try:
            withdraw(all_wallets[wallet_id], amount)
            print("Withdrawal successful")
        except ValueError as error:
            print(error)
    else:
        print("Wallet ID not found")


def handle_transfer(all_wallets):
    sender_id = input("Enter sender wallet ID: ")
    receiver_id = input("Enter receiver wallet ID: ")

    if sender_id in all_wallets and receiver_id in all_wallets:
        amount = float(input("Enter amount: "))
        try:
            transfer(all_wallets[sender_id], all_wallets[receiver_id], amount)
            print("Transfer successful")
        except ValueError as error:
            print(error)
    else:
        print("One or both wallet IDs not found")


def handle_show_wallet(all_wallets):
    wallet_id = input("Enter wallet ID: ")

    if wallet_id in all_wallets:
        show_wallet(all_wallets[wallet_id])
    else:
        print("Wallet ID not found")


def handle_show_history(all_wallets):
    wallet_id = input("Enter wallet ID: ")

    if wallet_id in all_wallets:
        show_history(all_wallets[wallet_id])
    else:
        print("Wallet ID not found")


def handle_save_wallets(all_wallets):
    save_wallets(all_wallets)
    print("All wallets saved successfully")


def handle_load_wallets():
    all_wallets = load_wallets()
    print("All wallets loaded successfully")
    return all_wallets


def handle_show_all_wallets(all_wallets):
    show_all_wallets(all_wallets)