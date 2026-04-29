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


