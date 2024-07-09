
class Bank:
    def __init__(self, name, accountNum):
        self._balance = 0
        self._name = name
        self._accountNum = accountNum
    def withdraw(self, amt):
        self._balance -= abs(amt)
    def deposit(self, amt):
        self._balance += abs(amt)
    def printAmt(self):
        return(self._balance)
    def printName(self):
        return(self._name)
    def printAccountNum(self):
        return(self._accountNum)