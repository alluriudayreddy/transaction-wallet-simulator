import random

def generate_wallet_id():
    return f'W{random.randint(1000,9999)}'


def show_wallet(wallet):
    print(f"Wallet ID: {wallet.wallet_id}")
    print(f'Owner: {wallet.owner}')
    print(f'Balance: {wallet.balance}')


def show_history(wallet):
    print("History:")
    for item in wallet.history:
        print(item)


def show_all_wallets(wallets):
    print("All Wallets: ")
    for wallet_id, wallet in wallets.items():
        print(f'{wallet_id}: {wallet.owner} - Balance: {wallet.balance} - History: {wallet.history}')
