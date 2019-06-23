'''
A bank account availing the options os withdrawal, deposit
'''
#Object oriented programming concept
class BankAccount():

    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
    
    def __str__(self): #To print the name and balance
        return f" The available balance in {self.name} account is {self.balance}\n Account owner: \t{self.name}\n Account balance: \t{self.balance}\n"
    
    def owner(self): #To return the account holder name
        return self.name

    def balance(self): #To return the balance amount
        return self.balance

    def deposit(self, damount): #To facilitate the deposit and add it to the balance
        print(f"The amount {damount} is successfully deposited into {self.name} account")
        self.balance = self.balance + damount

    def withdraw(self, wamount): #To facilitate the withdrawal option if the amount is available
        if wamount <= self.balance:
           print("Withdrawal Accepted")
           self.balance = self.balance - wamount
        else:
           print("Amount Unavailable")
           print(f"Enter the amount less than {self.balance}")

#User input
name = input("Enter your name:\t")
balance = int(input("Enter the balance available:\t"))
acct = BankAccount(name, balance)
print(acct)
#User's choice 
w_d = input("Choose your option\n [d] : \t deposit \n [w] : \t withdraw\n ")
if w_d == 'd':
   damount = int(input("Enter the amount you want to deposit:\t"))
   acct.deposit(damount)
elif w_d == 'w':
   wamount = int(input("Enter the amount you want to withdraw:\t"))
   acct.withdraw(wamount)
else:
   print("Option invalid\n")
print(acct)

