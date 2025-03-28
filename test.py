import pytest
from atm_controller import ATM 

class DummyDB():
    def __init__(self):
        # Sample data for testing
        self.sample_cid = "1111-2222-3333-4444"
        self.sample_pin = "0000"
        self.sample_accounts = ["12345", "67890"]
        self.sample_balance = {"12345": 1000, "67890": 500}

    def insert_card(self, cardid):
        return cardid == self.sample_cid
    
    def auth_card(self, cardid, pin):
        return cardid == self.sample_cid and pin == self.sample_pin
    
    def get_accounts(self, cardid):
        return self.sample_accounts
    
    def get_balance(self, account):
        return self.sample_balance[account]
    
    def set_balance(self, account, amount):
        self.sample_balance[account] = amount


@pytest.fixture
def sample_data():
    return DummyDB()

def test_insert_card(sample_data):

    atm = ATM(sample_data) 
    assert atm.insert_card(sample_data.sample_cid) == True
    assert atm.insert_card("0000-0000-0000-0000") == False
