from handlers import (
    handle_create_wallet,
    handle_deposit,
    handle_withdraw,
    handle_transfer,
    handle_show_wallet,
    handle_show_history,
    handle_save_wallets,
    handle_load_wallets,
    handle_show_all_wallets
)

wallets = {}

while True:
    print("\n--- Wallet Menu ---")
    print("1. Create Wallet")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Transfer")
    print("5. Show Wallet")
    print("6. Show History")
    print("7. Save Wallets")
    print("8. Load Wallets")
    print("9. Show All Wallets")
    print("10. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        handle_create_wallet(wallets)

    elif choice == "2":
        handle_deposit(wallets)

    elif choice == "3":
        handle_withdraw(wallets)

    elif choice == "4":
        handle_transfer(wallets)

    elif choice == "5":
        handle_show_wallet(wallets)

    elif choice == "6":
        handle_show_history(wallets)

    elif choice == "7":
        handle_save_wallets(wallets)

    elif choice == "8":
        wallets = handle_load_wallets()

    elif choice == "9":
        handle_show_all_wallets(wallets)

    elif choice == "10":
        print("Exiting...")
        break

    else:
        print("Invalid choice")