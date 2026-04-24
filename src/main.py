from model import Wallet

w1 = Wallet("w1", "Danam", 1280)
print("Owner:", w1.owner)
print("ID:", w1.wallet_id)
print("Balance:", w1.balance)
print("History:", w1.history)