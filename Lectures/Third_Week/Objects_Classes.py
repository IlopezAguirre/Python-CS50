###OBJECTS AND CLASSESS CHALLENGE
###----BANK ACCOUNT----

class BankAccount:
  def __init__(self,first_name, last_name, account_id, account_type, pin, balance):
    self.first_name = first_name
    self.last_name = last_name
    self.account_id = account_id
    self.account_type = account_type
    self.pin = pin
    self.balance = balance
  
  def deposit(self, money):
    self.balance += money
    return self.balance
  
  def withdraw(self, money):
    self.balance -= money
    return self.balance
  
  def display_balance(self):
    print(f'Current balance: {self.balance}')

person1 = BankAccount('Ian','Lopez', 123, 'savings',321, 0.0)

person1.deposit(96)
person1.withdraw(25)
person1.display_balance()
