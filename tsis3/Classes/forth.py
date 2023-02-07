class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f'Deposit of {amount} accepted.')
        print(f'Account balance: {self.balance}')

    def withdraw(self, amount):
        if amount > self.balance:
            print(f'Withdrawal of {amount} rejected. Insufficient funds.')
        else:
            self.balance -= amount
            print(f'Withdrawal of {amount} accepted.')
            print(f'Account balance: {self.balance}')
    
    def __str__(self):
        return f"the account information is the name :{self.owner}, and the balance is {self.balance}  "


name=str(input("enter the name of onwer    "))
balance= int(input ("enter the balance of the onwer   "))

account = BankAccount(name, balance)

print(account.__str__())

choose= int(input("for deposit enter 1 and for the withdraw enter 2 "))
if choose==1:
    de= int (input("how much do you want to deposit   ")) 
    account.deposit(de)
elif choose ==2:
    wi= int (input("how much do you want to withdraw  ")) 
    account.withdraw(wi)
else:
    print("wrong number read the instruction carefully")
