def deposit(wallet, amount):
    if amount <= 0:
        raise ValueError("Deposit amount must be positive.")
    wallet.balance += amount
    wallet.history.append(f'Deposited {amount}')
    return wallet.balance


def withdraw(wallet, amount):
    if amount <= 0:
        raise ValueError("Withdrawal amount must be positive.")
    
    if wallet.balance < amount:
        raise ValueError("Insufficient funds.")
    
    wallet.balance -= amount
    wallet.history.append(f'Withdrew {amount}')
    return wallet.balance


def transfer(sender_wallet, receiver_wallet, amount):
    if amount <= 0:
        raise ValueError("Transfer amount must be positive.")
    
    if sender_wallet.balance < amount:
        raise ValueError("Insufficient funds in sender's wallet.")
    
    sender_wallet.balance -= amount
    receiver_wallet.balance += amount
    
    sender_wallet.history.append(f'Transferred {amount} to {receiver_wallet.wallet_id}')
    receiver_wallet.history.append(f'Received {amount} from {sender_wallet.wallet_id}')
    
    return sender_wallet.balance, receiver_wallet.balance