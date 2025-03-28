
class ATM():
    def __init__(self, database):
        self.DB = database

    def deposit(self, amount):
        raise NotImplementedError("not implemented")

    def withdraw(self, amount):
        raise NotImplementedError("not implemented")
    
    def check_balance(self):
        raise NotImplementedError("not implemented")
    
    def insert_card(self, cardid):
        raise NotImplementedError("not implemented")
    
    def insert_pin(self, pin):
        raise NotImplementedError("not implemented")
    
    def get_accounts(self):
        raise NotImplementedError("not implemented")
    
    def select_account(self, account):
        raise NotImplementedError("not implemented")