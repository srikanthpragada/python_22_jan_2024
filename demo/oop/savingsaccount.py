class SavingsAccount:
    # Constructor
    def __init__(self, acno, ahname, balance=0):
        # object attributes
        self.acno = acno
        self.ahname = ahname
        # Private attribute
        self.__balance = balance

    # Methods

    def deposit(self, amount):
        self.__balance += amount


# create object
a1 = SavingsAccount(1, "Mark", 10000)
# call methods
a1.deposit(5000)

# Access object attribute
print(a1._SavingsAccount__balance)

print(a1.__dict__)


