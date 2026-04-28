from model import Wallet
from operations import deposit, withdraw, transfer
from storage import save_wallet, load_wallet

w1=Wallet("W001", "Danam", 1000)
w2=Wallet("W002", "Alice", 1500)

deposit(w1, 500)
transfer(w1, w2, 300)
withdraw(w1, 200)

save_wallet(w1)

loaded_wallet = load_wallet()

print(f'Owner: {loaded_wallet.owner}')
print(f'balance: {loaded_wallet.balance}')
print(f'History: {loaded_wallet.history}')

print(f'Sender Balance: {w1.balance}')
print(f'Receiver Balance: {w2.balance}')
print(f'Sender History: {w1.history}')
print(f'Receiver History: {w2.history}')