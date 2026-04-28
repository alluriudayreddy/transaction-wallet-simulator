from model import Wallet
from operations import deposit, withdraw, transfer
from storage import save_wallet, load_wallet
from helpers import generate_wallet_id, show_wallet, show_history


wallets = {}


while True:
    print("\n --- Wallet Menu---")
    print("1. Create Wallet")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Transfer")
    print("5. Show Wallet")
    print("6. Show Transaction History")
    print("7. Save Wallet")
    print("8. Load Wallet")
    print("9. Exit")


    choice = input ("Enter your choice: ")


    if choice == "1":
        owner = input("Enter wallet owner name: ")
        wallet_id = generate_wallet_id()
        wallets[wallet_id] = Wallet(wallet_id, owner, 0)
        print(f'Wallet created with ID: {wallet_id}')
