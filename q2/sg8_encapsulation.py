#Code

class BankAccount: #This is the class BankAccount.
    def __init__(self, account_number: int, balance: float): #This initializes the attributes once a class is made.
        self.set_account_number(account_number) #This is attribute 1.
        
        self.__balance = float(balance) #This is attribute 2.
        print("Account 1") #This prints "Account 1".
        print(f"Account Number: {self.__account_number}") #This prints "Account Number: ", followed by the account number given.
        print(f"Balance: {self.__balance:.2f}\n") #This prints "Balance: ", followed by the balance given from the object.

    def set_account_number(self, account_number: int): #This defines the public setter for the account number.
        self.__account_number = account_number #This assigns the value account_number to the private attribute self.__account_number.

    def set_balance(self, balance: float): #This defines public setter 1 for the balance.
        print(f"Update balance to {balance}") #This prints "Update balance to ", followed by the balance given from the object.
        if balance < 0: #This uses the if keyword to indicate that if the balance is less than 0, something will happen.
            print("The balance must not be a negative number.") #This issues a warning if the user enters a negative balance.
        else: #This indicates what will happen if the said condition is not fulfilled.
            self.__balance = float(balance) #This automatically prints the balance in decimal form (float).
        
        print(f"Account Number: {self.__account_number}") #This prints "Account Number: ", followed by the account number given.
        print(f"Balance: {self.__balance:.2f}\n") #This prints "Balance: ", followed by the balance given with 2 decimal places.

    @property #The @property decorator is for the public getter methods.
    def account_number(self): #This defines the method account_number().
        return self.__account_number #This returns the private attribute (account number).

    @property #The @property decorator is for the public getter methods.
    def balance(self): #This defines the method balance().
        return self.__balance #This returns the private attribute (balance).

#This is the Bank Account of Account 1, or object 1.
a1 = BankAccount(67890, 1000000) #This displays the first account's Account Number, followed by the balance.
a1.set_balance(999999) #This sets a positive balance, which will not display any warning and replace the original balance of 1000000.
a1.set_balance(-999999) #This sets a negative balance, which will display a warning and keep the original balance of 1000000.
