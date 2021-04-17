class Bank:
    bankname = "SBI"           # static variable : invoked using class name
    def acCreate(self, acno, name):
        self.acno = acno
        self.name = name
        self.minimumbal = 5000
        self.balance = self.minimumbal

    def deposit(self, amnt):
        self.balance += amnt
        print("your", Bank.bankname, "account has been credited with", amnt, "Rs")
        print("your current balance : ", self.balance)

    def withdraw(self, amnt):
        if amnt > self.balance:
            print("insufficient balance")
        else:
            self.balance -= amnt
            print("available balance : ", self.balance)


customer = Bank()
customer.acCreate(1001, "Arjun")
customer.deposit(25000)
customer.withdraw(12500)


# types of variables
# 1. static variable : invoked using class name
# 2. instance variable : invoked using self