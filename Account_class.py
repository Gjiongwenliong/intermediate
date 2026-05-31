# Create an Account class with:
# - name
# - account_type (asset, liability, equity, revenue, expense)
# - normal_balance ('debit' or 'credit')
# - balance (starting at 0)
# Add methods:
# - debit(amount): increases balance if normal_balance is debit, otherwise decreases
# - credit(amount): increases balance if normal_balance is credit, otherwise decreases
class Account:
    def __init__(self, name, account_type):
        self.name = name
        self.account_type = account_type
        self.normal_balance = self.determine_normal_balance()
        self.balance = 0

    def determine_normal_balance(self):
        if self.account_type in ['asset', 'expense']:
            return 'debit'
        elif self.account_type in ['liability', 'equity', 'revenue']:
            return 'credit'
        else:
            raise ValueError("Invalid account type")

    def debit(self, amount):
        if self.normal_balance == 'debit':
            self.balance += amount
        else:
            self.balance -= amount

    def credit(self, amount):
        if self.normal_balance == 'credit':
            self.balance += amount
        else:
            self.balance -= amount

    def __str__(self):
        return f"Account(name={self.name}, type={self.account_type}, balance={self.balance})"       
    #let user input the account details
def create_account():
    name = input("Enter account name: ")
    account_type = input("Enter account type (asset, liability, equity, revenue, expense): ")
    return Account(name, account_type)  
# main program to test the Account class
if __name__ == "__main__":
    account = create_account()
    print(account)
    while True:
        action = input("Enter 'debit' or 'credit' to update the account, or 'exit' to quit: ")
        if action == 'exit':
            break
        amount = float(input("Enter amount: "))
        if action == 'debit':
            account.debit(amount)
        elif action == 'credit':
            account.credit(amount)
        else:
            print("Invalid action. Please enter 'debit', 'credit', or 'exit'.")
        print(account)      
    