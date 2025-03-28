class DatabaseInterface():
    def is_exist_card_id(self, cardid):     
        raise NotImplementedError("not implemented")
    def auth_card(self, cardid, pin): 
        raise NotImplementedError("not implemented")
    def get_accounts(self, cardid):
        raise NotImplementedError("not implemented")
    def get_balance(self, account):
        raise NotImplementedError("not implemented")    
    def set_balance(self, account, amount):
        raise NotImplementedError("not implemented")