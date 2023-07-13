class Bank:
    def __init__(self, name, accountNum, balance=0): #default has to be at the end
        self.name = name
        self.accountNum= accountNum
        self.balance= balance
    

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance = self.balance - amount
        else:
            raise ValueError(f"You don't have enough money to withdraw {amount}.")

    def deposit(self, amount):
        self.balance = self.balance + amount

    def printBalance(self):
        print(self.balance)
    

if __name__ == "__main__":
    my = Bank("Swati", 500, 100.25)
    my.printBalance()
    my.withdraw(40)
    my.printBalance()
    my.deposit(40)
    my.printBalance()   