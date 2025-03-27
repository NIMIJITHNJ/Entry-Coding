# Question 3. Create a Class for a Bank Account

class BankAccount:
    def __init__(self, accountNumber, balance=0.0):                 # Initialising bank account with a given account number and an optional starting balance (by default set to 0).
        self.accountNumber = accountNumber
        self.balance = balance

    def deposit(self, amount):                                      # Function to deposit an amount greater than zero.
        if amount > 0:
            self.balance += amount
        else:
            raise ValueError("Deposit amount must be greater than 'Zero'!")

    def withdraw(self, amount):                                     # Function to withdraw an amount greater than zero.
        if amount <= 0:
            raise ValueError("Withdrawal amount must be greater than 'Zero'!")
        elif amount > self.balance:
            raise ValueError("Insufficient balance!")
        else:
            self.balance -= amount 

    def transfer(self, otherAccount, amount):                       # Function to transfer an amount greater than zero
        if amount <= 0:
            raise ValueError("Transfer amount must be greater than 'Zero'!")
        elif amount > self.balance:
            raise ValueError("Insufficient balance for transfer.")
        else:
            self.withdraw(amount)
            otherAccount.deposit(amount)

    def getBalance(self):                                           # Getter function for returning current balance
        return self.balance

def menu(accounts):                                                 # Menu function for user interaction.
    while True:                                                     # Starts a main loop
        print("\n--------------------------")
        print("     Account Dashboard    ")
        print("--------------------------")
        print("1. Deposit money")
        print("2. Withdraw money")
        print("3. Transfer money")
        print("4. Balance enquiry")
        print("5. Exit")
        print("--------------------------\n")
        choice = input("Enter your choice (1-5): ")                 # Collect user input for action choice.

        if choice == '1':                                           # Handles deposit action.
            while True:                                             
                accountNumber = input("\nEnter your account number: ")
                if accountNumber in accounts:                       # Check if the account number is in the dictionary.
                    try:
                        amount = float(input("Enter amount to be deposited: "))
                        accounts[accountNumber].deposit(amount)
                        print(f"An amount of ₹{amount} has been deposited. New balance in your account ({accountNumber}) is ₹{accounts[accountNumber].getBalance():.2f}")
                        break                                       # Exit the loop after successfull deposit transaction with a feedback.
                    except ValueError as e:
                        print(e)
                        if input("Would you like to try again? (yes/no): ").lower() != 'yes':
                            break                                   # Exist the loop if the user does not want to try again after raising an error.  
                else:
                    print("Invalid account number! Please enter your 7 digit account number.")
                    if input("Would you like to try again? (yes/no): ").lower() != 'yes':                
                        break                                       # Exit the loop if the user does not want to try again  
            if input("Would you like to go back main menu? (yes/no): ").lower() != 'yes':
                print("Exiting....")                                
                break                                               # Exit the programme if the user does not want to go back to main menu.                  

        elif choice == '2':                                         # Handles withdrawal action.            
            while True:
                accountNumber = input("\nEnter your account number: ")
                if accountNumber in accounts:                       # Check if the account number is in the dictionary.
                    try:    
                        amount = float(input("Enter amount to be withdrawn: "))
                        accounts[accountNumber].withdraw(amount)
                        print(f"An amount of ₹{amount} has been withdrawn. Remaining balance in your account ({accountNumber}) is ₹{accounts[accountNumber].getBalance():.2f}")
                        break                                       # Exit the loop after successfull withdrawal transaction with a feedback.
                    except ValueError as e:
                        print(e)
                        if input("Would you like to try again? (yes/no): ").lower() != 'yes':
                            break                                   # Exist the loop if the user does not want to try again after raising an error.                
                else:
                    print("Invalid account number! Please enter your 7 digit account number.")
                    if input("Would you like to try again? (yes/no): ").lower() != 'yes':                
                        break                                       # Exit the loop if the user does not want to try again. 
            if input("Would you like to go back main menu? (yes/no): ").lower() != 'yes':
                print("Exiting....")    
                break                                               # Exit the programme if the user does not want to go back to main menu.

        elif choice == '3':                                         # Handles transfer action. 
            while True:            
                sourceAccount = input("\nEnter your account number: ")
                if sourceAccount in accounts:                       # Check if the account number is in the dictionary.
                    targetAccount = input("Enter target account number: ")
                    if targetAccount in accounts:                   # Check if the account number is in the dictionary.    
                        try:
                            amount = float(input("Enter amount to be transferred: "))
                            accounts[sourceAccount].transfer(accounts[targetAccount], amount)
                            print(f"An amount of ₹{amount} has been transferred from {sourceAccount} to {targetAccount} . New balance in your account is ₹{accounts[sourceAccount].getBalance():.2f}")
                            break                                   # Exit the loop after successfull transfer transaction with a feedback.
                        except ValueError as e:
                            print(e)
                            if input("Would you like to try again? (yes/no): ").lower() != 'yes':
                                break                               # Exist the loop if the user does not want to try again after raising an error. 
                    else:
                        print("Invalid account number! Please enter the 7 digit account number.")
                        if input("Would you like to try again? (yes/no): ").lower() != 'yes':                
                            break                                   # Exit the loop if the user does not want to try again. 
                else:
                    print("Invalid account number! Please enter your 7 digit account number.")
                    if input("Would you like to try again? (yes/no): ").lower() != 'yes':                
                        break                                       # Exit the loop if the user does not want to try again. 
            if input("Would you like to go back main menu? (yes/no): ").lower() != 'yes':                        
                print("Exiting....")    
                break                                               # Exit the programme if the user does not want to go back to main menu.

        elif choice == '4':                                         # Handles balance enquiry action.
            while True:           
                accountNumber = input("\nEnter your account number: ")
                if accountNumber in accounts:                       # Check if the account number is in the dictionary.                    
                        print(f"Current balance: ₹{accounts[accountNumber].getBalance():.2f}")
                        break                                       # Exit the loop after successfull trabalance enquiry with a feedback.
                else:
                    print("Invalid account number! Please enter your 7 digit account number.")
                    if input("Would you like to try again? (yes/no): ").lower() != 'yes':                
                        break                                       # Exit the loop if the user does not want to try again. 
            if input("Would you like to go back main menu? (yes/no): ").lower() != 'yes':   
                print("Exiting....")                                # Exit the programme if the user does not want to go back to main menu.
                break  

        elif choice == '5':                                         # Handles exit action.
            print("Exiting....")
            break                                                  

        else:
            print("\nInvalid choice! Please select 1-5.")           # Feedback for invalid user input.

if __name__ == "__main__":                                          # Main block for initialising dummy accounts and launch the menu interaction.
    accounts = {
        "6730001": BankAccount("6730001"),
        "6730002": BankAccount("6730002", 10000.0),
        "6730003": BankAccount("6730003", 50000.0),
        "6730004": BankAccount("6730004", 24535.50),
        "6730005": BankAccount("6730005", 10025.70)
    }
    menu(accounts)