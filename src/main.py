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
from storage import load_wallets


def main():
    all_wallets = load_wallets()

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

        menu_choice = input("Enter choice: ")

        if menu_choice == "1":
            handle_create_wallet(all_wallets)

        elif menu_choice == "2":
            handle_deposit(all_wallets)

        elif menu_choice == "3":
            handle_withdraw(all_wallets)

        elif menu_choice == "4":
            handle_transfer(all_wallets)

        elif menu_choice == "5":
            handle_show_wallet(all_wallets)

        elif menu_choice == "6":
            handle_show_history(all_wallets)

        elif menu_choice == "7":
            handle_save_wallets(all_wallets)

        elif menu_choice == "8":
            all_wallets = handle_load_wallets()

        elif menu_choice == "9":
            handle_show_all_wallets(all_wallets)

        elif menu_choice == "10":
            print("Exiting...")
            break

        else:
            print("Invalid menu choice")


if __name__ == "__main__":
    main()
