from model import Wallet
from operations import deposit, withdraw, transfer
from storage import save_wallets, load_wallets
from helpers import generate_wallet_id, show_wallet, show_history, show_all_wallets

def handle_create_wallet(wallets):
    owner = input("Enter owner name: ")
    wallet_id = generate_wallet_id()
    wallets[wallet_id] = Wallet(wallet_id, owner, 0)
    print(f"Wallet created with ID: {wallet_id}")



def handle_deposit(wallets):
    wallet_id = input("Enter wallet ID: ")

    if wallet_id in wallets:
        amount = float(input("Enter amount: "))
        try:
            deposit(wallets[wallet_id], amount)
            print("Deposit successful")
        except ValueError as e:
            print(e)
    else:
        print("Wallet ID not found")



def handle_withdraw(wallets):
    wallet_id = input("Enter wallet ID: ")

    if wallet_id in wallets:
        amount = float(input("Enter amount: "))
        try:
            withdraw(wallets[wallet_id], amount)
            print("Withdrawal successful")
        except ValueError as e:
            print(e)
    else:
        print("Wallet ID not found")



def handle_transfer(wallets):
    sender_id = input("Enter sender wallet ID: ")
    receiver_id = input("Enter receiver wallet ID: ")

    if sender_id in wallets and receiver_id in wallets:
        amount = float(input("Enter amount: "))
        try:
            transfer(wallets[sender_id], wallets[receiver_id], amount)
            print("Transfer successful")
        except ValueError as e:
            print(e)
    else:
        print("One or both wallet IDs not found")



def handle_show_wallet(wallets):
    wallet_id = input("Enter wallet ID: ")

    if wallet_id in wallets:
        show_wallet(wallets[wallet_id])
    else:
        print("Wallet ID not found")



def handle_show_history(wallets):
    wallet_id = input("Enter wallet ID: ")

    if wallet_id in wallets:
        show_history(wallets[wallet_id])
    else:
        print("Wallet ID not found")



def handle_save_wallets(wallets):
    save_wallets(wallets)
    print("All Wallets saved successfully")



def handle_load_wallets():
    wallets = load_wallets()
    print("All wallets loaded successfully")
    return wallets



def handle_show_all_wallets(wallets):
    show_all_wallets(wallets)
