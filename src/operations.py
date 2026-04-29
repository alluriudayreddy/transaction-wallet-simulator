def deposit(wallet_account, amount):
    if amount <= 0:
        raise ValueError("Deposit amount must be positive.")
    wallet_account.balance += amount
    wallet_account.history.append(f'Deposited {amount}')
    return wallet_account.balance


def withdraw(wallet_account, amount):
    if amount <= 0:
        raise ValueError("Withdrawal amount must be positive.")
    
    if wallet_account.balance < amount:
        raise ValueError("Insufficient funds.")
    
    wallet_account.balance -= amount
    wallet_account.history.append(f'Withdrew {amount}')
    return wallet_account.balance


def transfer(sender_wallet_account, receiver_wallet_account, amount):
    if amount <= 0:
        raise ValueError("Transfer amount must be positive.")
    
    if sender_wallet_account.balance < amount:
        raise ValueError("Insufficient funds in sender's wallet.")
    
    sender_wallet_account.balance -= amount
    receiver_wallet_account.balance += amount
    
    sender_wallet_account.history.append(f'Transferred {amount} to {receiver_wallet_account.wallet_id}')
    receiver_wallet_account.history.append(f'Received {amount} from {sender_wallet_account.wallet_id}')
    
    return sender_wallet_account.balance, receiver_wallet_account.balance