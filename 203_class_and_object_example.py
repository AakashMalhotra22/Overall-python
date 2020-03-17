class Account:
    def __init__(self, owner, balance):
        self.owner = owner
        self. balance = balance

    def __str__(self):
        return(f"Account holder name: {self.owner}\nAccount balance: {self.balance}")
    def deposit(self,amount):
        if amount> 0:

           self.balance+=amount
           print("Cash credited to your account.")
        else:
            print("you cannot enter this try again")
    def withdraw(self, cash):
        if cash <= self.balance:
            print(f"This is your Rs {cash}.")
            self.balance-=cash
        else:
            print("Unsufficient funds in your account.")


if __name__ == "__main__":
    a1 = Account("Aakash_Malhotra", 100)
    print(a1)

    a1.deposit(10000)
    print(a1)
    a1.withdraw(500)
    print(a1.balance)
    print(a1)
    (a1.withdraw(10000000))
