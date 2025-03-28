
class ATM():
    def __init__(self, database):
        self.DB = database
        self.cardid = None
        self.authorized = False

    def deposit(self, amount):
        raise NotImplementedError("not implemented")

    def withdraw(self, amount):
        raise NotImplementedError("not implemented")
    
    def check_balance(self):
        raise NotImplementedError("not implemented")
    
    def insert_card(self, cardid):
        self._reset()
        if self.DB.is_exist_card_id(cardid):
            self.cardid = cardid
            return True
        else:
            return False
    
    def insert_pin(self, pin):
        if self.cardid is None:
            return False        
        if self.DB.auth_card(self.cardid, pin):
            self.authorized = True
            return True
        return False

    def get_accounts(self):
        raise NotImplementedError("not implemented")
    
    def select_account(self, account):
        raise NotImplementedError("not implemented")
    
    def _reset(self):
        self.cardid = None
        self.authorized = False