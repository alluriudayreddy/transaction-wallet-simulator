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


def transfer(sender, receiver, amount):
    if amount <= 0:
        raise ValueError("Transfer amount must be positive.")
    
    if sender.balance < amount:
        raise ValueError("Insufficient funds in sender's wallet.")
    
    sender.balance -= amount
    receiver.balance += amount

    sender.history.append(f'Transferred {amount} to {receiver.owner}')
    receiver.history.append(f'Received {amount} from {sender.owner}')
    
    return sender.balance, receiver.balance
