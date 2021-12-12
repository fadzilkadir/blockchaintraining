class DevAccount(Account):
    def getbalance(self):
        return self.balance
    
    def setbalance(self,amount):
        self.balance = amount
        
d = DevAccount("Adam",100)
print(f"balance:{d.getbalance()}")
d.setbalance(95)
print(f"balance:{d.getbalance()}")