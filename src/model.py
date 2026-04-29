class WalletAccount:

    def __init__(self, wallet_id, owner, balance):
        self.wallet_id = wallet_id
        self.owner = owner
        self.__balance =  balance
        self.history = []


    @property
    def balance(self):
        return self.__balance
    
    @property
    def history(self):
        return self.__history
    

    def add_balance(self, amount):
        self.__balance += amount
        
    def subtract_balance(self, amount):
        self.__balance -= amount

    def add_history(self, message):
        self.history.append(message)