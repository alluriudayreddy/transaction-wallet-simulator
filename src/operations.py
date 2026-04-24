def deposit(wallet, amount):
    if amount <= 0:
        raise ValueError("Deposit amount must be positive.")
    wallet.balance += amount
    wallet.history.append(f'Deposited {amount}')
    return wallet.balance