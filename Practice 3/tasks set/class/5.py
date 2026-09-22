class Account:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print("Deposited:", amount)

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print("Withdrawn:", amount)
        else:
            print("Not enough balance")

    def show_balance(self):
        print("Owner:", self.owner)
        print("Balance:", self.balance)

account = Account("Adina", 1000)
account.deposit(500)
account.withdraw(200)
account.withdraw(2000)
account.show_balance()