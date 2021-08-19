# David Martinez
# Class Challenge 2

# Create a bank account class that has two attributes:
#     - Owner
#     - balance
#
# and two methods:
#     - deposit
#     - withdraw
#
# As an added requirement, withdrawals may not exceed the available balance.
#
# Instantiate your class, make several deposits and withdrawals, and test to
#     make sure the account can't be overdrawn.

class Bank_Account:

    def __init__(self):
        self.owner = 'David'
        self.balance = 0.00     # set start balance

    def welcome(self):
        while True:      # loop to stay in until user quits
            print(f'Your account balance is ${round(self.balance,2)}.')
            choice = input('Choices are: (d)eposit, (w)ithdrawal, or (q)uit: ')
            if choice == 'd':
                atm.deposit()
            elif choice == 'w':
                atm.withdraw()
            elif choice == 'q':
                print('Goodbye')
                break

    def deposit(self):
        deposit = input('Enter deposit amount: $')          # deposit input from user
        self.balance += round(float(deposit),2)             # add the deposit to the balance
        print(f'Your new balance is {self.balance}.')       # print new balance

    def withdraw(self):
        withdrawal = input('Enter withdrawal amount: $')    # deposit input from user
        if round(float(withdrawal),2) > self.balance:       # checking you have enough money
            print('You do not have enough funds for this request.\n')
        else:
            self.balance -= float(withdrawal)               # subtract the withdrawal from balance
            print(f'Your new balance is {self.balance}.')   # print new balance

atm = Bank_Account()    # instance
atm.welcome()           # start the welcome method
