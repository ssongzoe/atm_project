
class ATM():
    def __init__(self, database):
        self.DB = database
        self.cardid = None
        self.authorized = False
        self.accounts = None
        self.account = None

    def deposit(self, amount):
        if not self.authorized:
            return False
        if self.accounts is None:
            return False
        if self.account is None:
            return False
        if amount <= 0:
            return False
        if self.DB.set_balance(self.account, amount):
            return True
        return False

    def withdraw(self, amount):
        if not self.authorized:
            return False
        if self.accounts is None:
            return False
        if self.account is None:
            return False
        if amount <= 0:
            return False
        if amount > self.DB.get_balance(self.account):
            return False
        if self.DB.set_balance(self.account, -amount):
            return True
        return False

    
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
        if not self.authorized:
            return False
        self.accounts = self.DB.get_accounts()
        return self.accounts
    
    def select_account(self, account):
        if not self.authorized:
            return False
        if account in self.accounts:
            self.account = account
            return True
        return False

    def check_balance(self):
        if not self.authorized:
            return False
        if self.accounts is None:
            return False
        if self.account is None:
            return False
        return self.DB.get_balance(self.account)
    
    def _reset(self):
        self.cardid = None
        self.authorized = False