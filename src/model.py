class WalletAccount:
    
    def __init__(self, wallet_id, owner, balance):
        self.wallet_id = wallet_id
        self.owner = owner
        self.balance = balance
        self.history = []