class Bank:
    def __init__(self, balance, name, accountNum):
        self.balance = balance
        self.name = name
        self.accountnum = accountNum
    def withdraw(self, amt):
        self._balance -= amt
    def deposit(self, amt):
        self._balance += amt
    def printAmt(self):
        print(self._balance)