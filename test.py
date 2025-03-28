import pytest
from atm_controller import ATM 

class DummyDB():
    def __init__(self):
        # Sample data for testing
        self.sample_cid = "1111-2222-3333-4444"
        self.sample_pin = "0000"
        self.sample_accounts = ["12345", "67890"]
        self.sample_balance = {"12345": 1000, "67890": 500}

    def is_exist_card_id(self, cardid):
        return cardid == self.sample_cid
    
    def auth_card(self, cardid, pin): #비밀번호
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
# normal scenario
def test_insert_valid_card(sample_data):
    atm = ATM(sample_data) 
    assert atm.insert_card(sample_data.sample_cid) == True

def test_insert_invalid_card(sample_data):
    atm = ATM(sample_data) 
    assert atm.insert_card("0000-0000-0000-0000") == False

def test_insert_valid_pin(sample_data):
    atm = ATM(sample_data)
    assert atm.insert_card(sample_data.sample_cid) == True    
    assert atm.insert_pin(sample_data.sample_pin) == True

def test_insert_invalid_pin(sample_data):
    atm = ATM(sample_data)
    assert atm.insert_card(sample_data.sample_cid) == True
    assert atm.insert_pin("1234") == False

def test_get_accounts(sample_data):
    atm = ATM(sample_data)
    assert atm.insert_card(sample_data.sample_cid) == True    
    assert atm.insert_pin(sample_data.sample_pin) == True
    assert atm.get_accounts() == sample_data.sample_accounts

def test_valid_select_account(sample_data):
    atm = ATM(sample_data)
    assert atm.insert_card(sample_data.sample_cid) == True
    assert atm.insert_pin(sample_data.sample_pin) == True
    assert atm.select_account(sample_data.sample_accounts[0]) == True
    assert atm.select_account(sample_data.sample_accounts[1]) == True

def test_invalid_select_account(sample_data):
    atm = ATM(sample_data)
    assert atm.insert_card(sample_data.sample_cid) == True
    assert atm.insert_pin(sample_data.sample_pin) == True
    assert atm.select_account("00000") == False

def test_check_balance(sample_data):
    atm = ATM(sample_data)
    assert atm.insert_card(sample_data.sample_cid) == True    
    assert atm.insert_pin(sample_data.sample_pin) == True
    assert atm.select_account(sample_data.sample_accounts[0]) == True
    assert atm.check_balance() == sample_data.sample_balance[sample_data.sample_accounts[0]]
    assert atm.select_account(sample_data.sample_accounts[1]) == True
    assert atm.check_balance() == sample_data.sample_balance[sample_data.sample_accounts[1]]   

def test_deposit(sample_data):
    atm = ATM(sample_data)
    assert atm.insert_card(sample_data.sample_cid) == True
    assert atm.insert_pin(sample_data.sample_pin) == True
    assert atm.select_account(sample_data.sample_accounts[0]) == True
    initial_balance = atm.check_balance()
    assert atm.deposit(100) == True
    assert atm.check_balance() == initial_balance + 100

def test_invaild_deposit(sample_data):
    atm = ATM(sample_data)
    assert atm.insert_card(sample_data.sample_cid) == True
    assert atm.insert_pin(sample_data.sample_pin) == True
    assert atm.select_account(sample_data.sample_accounts[0]) == True
    initial_balance = atm.check_balance()
    assert atm.deposit(-100) == False
    assert atm.check_balance() == initial_balance    

def test_withdraw(sample_data):
    atm = ATM(sample_data)
    assert atm.insert_card(sample_data.sample_cid) == True
    assert atm.insert_pin(sample_data.sample_pin) == True
    assert atm.select_account(sample_data.sample_accounts[0]) == True
    initial_balance = atm.check_balance()
    assert atm.withdraw(initial_balance - 100) == True
    assert atm.check_balance() == 100

def test_invalid_withdraw(sample_data):
    atm = ATM(sample_data)
    assert atm.insert_card(sample_data.sample_cid) == True
    assert atm.insert_pin(sample_data.sample_pin) == True
    assert atm.select_account(sample_data.sample_accounts[0]) == True
    initial_balance = atm.check_balance()
    assert atm.withdraw(initial_balance + 100) == False
    assert atm.check_balance() == initial_balance

def test_invalid_order(sample_data):
    atm1 = ATM(sample_data)
    assert atm1.insert_pin(sample_data.sample_pin) == False

    atm2 = ATM(sample_data)
    assert atm2.get_accounts() == False

    atm3 = ATM(sample_data)
    assert atm3.select_account(sample_data.sample_accounts[0]) == False

    atm4 = ATM(sample_data)
    assert atm4.check_balance() == False

    atm5 = ATM(sample_data)
    assert atm5.deposit(100) == False

    atm6 = ATM(sample_data)
    assert atm6.withdraw(100) == False

def test_auth_reset(sample_data):
    atm = ATM(sample_data)
    assert atm.insert_card(sample_data.sample_cid) == True
    assert atm.insert_pin(sample_data.sample_pin) == True
    assert atm.get_accounts() == sample_data.sample_accounts
    assert atm.select_account(sample_data.sample_accounts[0]) == True
    assert atm.check_balance() == sample_data.sample_balance[sample_data.sample_accounts[0]]
    assert atm.deposit(100) == True
    assert atm.withdraw(100) == True
  
    # reinsert the card
    assert atm.insert_card(sample_data.sample_cid) == True
    assert atm.get_accounts() == False
    assert atm.select_account(sample_data.sample_accounts[0]) == False
    assert atm.check_balance() == False
    assert atm.deposit(100) == False
    assert atm.withdraw(100) == False