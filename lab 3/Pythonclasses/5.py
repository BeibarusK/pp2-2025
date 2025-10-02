class Account():
    def __init__(self, owner, balance):
        self.owner=owner
        self.balance=balance
    def withdraw(self):
        money=int(input("How much money do u want to withdraw? "))
        if self.balance<money:
            print("It s not possible")
        else:
            self.balance-=money
            print("Withdraw went successfully!")

    def deposit(self):
        money=int(input("How much money do u want to deposit? "))
        self.balance+=money
        print("Deposit went successfully!")
a=Account("Beibarys",10000)
a.withdraw()
a.deposit()
print(a.balance)