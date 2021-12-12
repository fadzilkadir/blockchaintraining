class Account: 
    idcnt = 1
    
    def __init__(self, name, balance):
        self.id = Account.idcnt
        Account.idcnt += 1
        self.name = name
        self.balance = balance
        
    def _deposit(self, amount):
        self.balance += amount
        
    def _withdraw(self, amount):
        if amount < self.balance:
            self.balance -= amount
        
    def __str__(self):
        return f"name:{self.name}\nid:{self.id}\nbalance:{self.balance}"
        
a = Account("Adam", 1000)
b = Account("Rachel",2500)
c = Account("John",5000)
print(f"{a}\n{b}\n{c}")