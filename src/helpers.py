import random

def generate_wallet_id():
    return f'W{random.randint(1000,9999)}'


def show_wallet(wallet_account):
    print(f"Wallet ID: {wallet_account.wallet_id}")
    print(f'Owner: {wallet_account.owner}')
    print(f'Balance: {wallet_account.balance}')


def show_history(wallet_account):
    print("History:")
    for item in wallet_account.history:
        print(item)


def show_all_wallets(all_wallets):
    print("All Wallets: ")
    for wallet_id, wallet_account in all_wallets.items():
        print(f'{wallet_id}: {wallet_account.owner} - Balance: {wallet_account.balance} - History: {wallet_account.history}')
