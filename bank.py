
class Bank:
    def __init__(self, name, accountNum):
        self.balance = 0
        self.name = name
        self.accountNum = accountNum
    def withdraw(self, amt):
        self.balance -= abs(amt)
    def deposit(self, amt):
        self.balance += abs(amt)
    def printAmt(self):
        return(self.balance)
    def printName(self):
        return(self.name)
    def printAccountNum(self):
        return(self.accountNum)