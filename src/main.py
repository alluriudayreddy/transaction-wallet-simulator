from model import Wallet
from operations import deposit, withdraw, transfer
from storage import save_wallets, load_wallets
from helpers import generate_wallet_id, show_wallet, show_history


wallets = {}


while True:
    print("\n--- Wallet Menu ---")
    print("1. Create Wallet")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Transfer")
    print("5. Show Wallet")
    print("6. Show History")
    print("7. Save Wallet")
    print("8. Load Wallet")
    print("9. Exit")


    choice = input("Enter choice: ")

    if choice == "1":
        owner = input("Enter owner name: ")
        wallet_id = generate_wallet_id()
        wallets[wallet_id] = Wallet(wallet_id, owner, 0)
        print(f"Wallet created with ID: {wallet_id}")
        print(wallets.keys())


    elif choice == "2":
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



    elif choice == "3":
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



    elif choice == "4":
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
            print("Invalid sender or receiver ID")



    elif choice == "5":
        wallet_id = input("Enter wallet ID: ")

        if wallet_id in wallets:
            show_wallet(wallets[wallet_id])
        else:
            print("Wallet ID not found")



    elif choice == "6":
        wallet_id = input("Enter wallet ID: ")

        if wallet_id in wallets:
            show_history(wallets[wallet_id])
        else:
            print("Wallet ID not found")


    elif choice == "7":
        print(wallets)
        print(wallets.keys())
        save_wallets(wallets)
        print("All wallets saved")

    elif choice == "8":
        wallets = load_wallets()
        print("All wallets loaded")


    elif choice == "9":
        print("Exiting...")
        break



    else:
        print("Invalid choice")