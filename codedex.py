#First type
class BankAccount:
  def __init__(self,first_name,last_name,account_id,account_type,pin,balance):
    self.first_name = first_name
    self.last_name = last_name
    self.account_id = account_id
    self.account_type = account_type
    self.pin = pin 
    self.balance = balance

  def deposit(self,pin):
    self.balance += pin
    print(f"You add:{pin }in you account and now you account have{self.balance}")
  
  def withdraw(self,pin):
    self.balance -= pin
    print(f'You account process{-pin} from balance and  you get{pin}')
  
  def display_balance(self):
    print(f"You account have {self.balance}")

G = BankAccount('Jia','Ni',1717,'save account',0,1000)
print(vars(G))

G.deposit(96)
G.withdraw(25)
G.display_balance()



# Update new method, use the return + word and int

class BankAccount:
  def __init__(self,first_name,last_name,account_id,account_type,pin,balance):
    self.first_name = first_name
    self.last_name = last_name
    self.account_id = account_id
    self.account_type = account_type
    self.pin = pin 
    self.balance = balance

  def deposit(self,pin):
    self.balance += pin
    return f"You added {pin}, balance is now {self.balance}"
  
  def withdraw(self,pin):
    self.balance -= pin
    return f"You get{pin}, balance is now {self.balance}"

  def display_balance(self):
    return f"Now you account still have{self.balance}"

G = BankAccount('Jia','Ni',1717,'save account',0,1000)
print(vars(G))

print(G.deposit(96))
print(G.withdraw(25))
print(G.display_balance())
