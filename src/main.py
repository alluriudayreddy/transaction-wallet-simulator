from model import Wallet
from operations import deposit, withdraw


w1 = Wallet("w1", "Danam", 1280)

try:
    deposit(w1, 300)
    withdraw(w1, 200)
    withdraw(w1, 5000)

except ValueError as e:
    print("Error:", e)

print(f'balance {w1.balance}')
print("History:", w1.history)