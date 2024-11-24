import datetime
import pandas as pd
import os

today = datetime.date.today()
formatted_date = today.strftime('%d/%m/%Y')

class Account:
    # Attributes
    fileName = "Accounts.csv"
    firstName = ""
    lastName = ""
    aadharNumber = ""
    AccNo = 0
    Pin = -1
    Balance = 0
    accounts_df = pd.DataFrame(columns=["AccountNumber", "FirstName", "LastName", "AadharNumber", "Pin", "Balance"])

    # Constructor
    # Load data from CSV if it exists, otherwise create an empty DataFrame
    def __init__(self):
        if os.path.exists(self.fileName):
            self.accounts_df = pd.read_csv(self.fileName)
        else:
            self.accounts_df = pd.DataFrame(columns=["AccountNumber", "FirstName", "LastName", "AadharNumber", "Pin", "Balance"])
    # Save DataFrame to CSV
    def save_to_file(self):
        self.accounts_df.to_csv(self.fileName, index=False)
    def EraseAllData(self):
            self.accounts_df = pd.DataFrame(columns=["AccountNumber", "FirstName", "LastName", "AadharNumber", "Pin", "Balance"])
            print("\n---All the data from the Database Has been Removed...\n")
    def Input(self):
        # Taking user input for account details
        self.firstName = input("Enter your First name: ")
        self.lastName = input("Enter your Last name: ")
        self.aadharNumber = input("Enter your Aadhar number: ")
        self.Pin = int(input("Set your 4 Digit Pin number: "))
        self.Balance = int(input("Enter your Initial Balance : "))  # You can set an initial balance if needed

        # Get the last account number and increment it
        lastAccNo = self.accounts_df["AccountNumber"].max() if not self.accounts_df.empty else 0
        newAccNo = lastAccNo + 1

        # Create a new account record
        newAccount = {
            "AccountNumber": newAccNo,
            "FirstName": self.firstName,
            "LastName": self.lastName,
            "AadharNumber": self.aadharNumber,
            "Pin": self.Pin,
            "Balance": self.Balance
        }

        # Append the new account to the DataFrame
        newAccountDf = pd.DataFrame([newAccount])
        self.accounts_df = pd.concat([self.accounts_df, pd.DataFrame(newAccountDf)], ignore_index=True)
        self.save_to_file()
        print("\n--- Account Created Successfully :)\n")

    def display(self):
        # Display the account details in DataFrame
        print("\n--- Displaying All Accounts ---")
        print(self.accounts_df)
        print("----------------------------------")
    
    def update_balance(self, account_number, new_balance):
        # Checking
        if account_number in self.accounts_df["AccountNumber"].values:
            # Update balance
            self.accounts_df.loc[self.accounts_df["AccountNumber"] == account_number, "Balance"] += new_balance
            print(f"--- Balance updated for Account Number {account_number} ---")
            self.save_to_file()
        else:
            print(f"--- Account Number '{account_number}' not found! ---")


# Main
print("\n**************************** Welcome to State Bank of India *************************************")
choice = 0
obj = Account()
while True:
    print("\t1. Open Bank Account.")
    print("\t2. Display Bank Accounts.")
    print("\t3. Deposit Money.")
    print("\t4. Withdraw Money.")
    print("\t5. Exit.")

    choice = int(input("Enter your Choice: "))
    if choice == 1:
        obj.Input()
    elif choice == 2:
        obj.display()
    elif choice == 3:
        obj.display()
        acc = int(input("Enter your Account number : "))
        money = int(input("Enter the Amount to be Deposited : "))
        obj.update_balance(acc,money)
    elif choice == 4:
        obj.display()
        acc = int(input("Enter your Account number : "))
        money = int(input("Enter the Amount to be WithDrawn : "))
        withdraw = -money
        obj.update_balance(acc,withdraw)
    else:
        break
