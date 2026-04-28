from model import Wallet
from operations import deposit, withdraw, transfer
from storage import save_wallet, load_wallet
from helpers import generate_wallet_id, show_wallet, show_history

wallets = {}

while True:
    print("\n --- Wallet Menu---")
    