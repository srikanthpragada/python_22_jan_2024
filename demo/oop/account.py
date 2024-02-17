class Account:
    minbal = 10000
    # Constructor
    def __init__(self, acno, ahname, balance=0):
        # object attributes
        self.acno = acno
        self.ahname = ahname
        self.balance = balance

    # Methods
    def show(self):
        print(f'Account Number : {self.acno}')
        print(f'Account Holder : {self.ahname}')
        print(f'Account Balance: {self.balance}')

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance - Account.minbal >= amount:
             self.balance -= amount
        else:
            print("Insufficient Balance!")

# create object
a1 = Account(1, "Mark", 10000)
# call methods
a1.deposit(5000)
a1.show()
# Access object attribute
print(a1.balance)


a2 = Account(2, "Joe")
