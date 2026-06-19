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


##Pokedex Challenge##
class Pokemon:
  def __init__(self, entry, name, types, description, is_caught):
    self.entry = entry
    self.name = name 
    self.types = types
    self.description = description
    self.is_caught = is_caught

  def speak(self):
    print(self.name + ' ' + self.name)

  def display_details(self):
    if self.is_caught == True:
      print(f'Entry Number: {self.entry}\nName: {self.name}\nType: {self.types}\nDescription: {self.description}\n{self.name} has already been caught')
    else:
         print(f'Entry Number: {self.entry}\nName: {self.name}\nType: {self.types}\nDescription: {self.description}\n{self.name} has not been caught')
    print()

Pikachu = Pokemon('25','Pikachu','Electric', 'It has small electric sacs on both its cheeks.' , True)
Torterra = Pokemon('381', 'Torterra', 'Plant','Some Pokémon are born on a Torterra’s back and spend their entire life there.', True)
Greninja = Pokemon('658', 'Greninja', 'Water', "Silent and Sneaky as a Ninja", True)

Pikachu.display_details()
Torterra.display_details()
Greninja.display_details()
Pikachu.speak()
Torterra.speak()
Greninja.speak()
