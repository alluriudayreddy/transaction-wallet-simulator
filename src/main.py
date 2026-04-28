from model import Wallet
from operations import deposit, withdraw
from storage import save_wallet, load_wallet

w1=Wallet("W001", "Danam", 1000)

deposit(w1, 500)
withdraw(w1, 200)

save_wallet(w1)

loaded_wallet = load_wallet()

print(f'Owner: {loaded_wallet.owner}')
print(f'balance: {loaded_wallet.balance}')
print(f'History: {loaded_wallet.history}')