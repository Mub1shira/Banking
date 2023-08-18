class BankAccount:
    def __init__(self, account_number, pin, balance=0):
        self.account_number = account_number
        self.pin = pin
        self.balance = balance

    def login(self, entered_account_number, entered_pin):
        if entered_account_number == self.account_number and entered_pin == self.pin:
            return True
        else:
            return False

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return True
        else:
            return False

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            return True
        else:
            return False

# Create a sample bank account
account_number = '123456'
pin = '1234'
initial_balance = 1000
bank_account = BankAccount(account_number, pin, initial_balance)

# Simulate user interaction
print("Welcome to the Banking System")
entered_account_number = input("Enter your account number: ")
entered_pin = input("Enter your PIN: ")

if bank_account.login(entered_account_number, entered_pin):
    print("Login successful")
    while True:
        print("\n1. Deposit\n2. Withdraw\n3. Check Balance\n4. Exit")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            amount = float(input("Enter the amount to deposit: "))
            if bank_account.deposit(amount):
                print("Deposit successful")
            else:
                print("Invalid amount")

        elif choice == 2:
            amount = float(input("Enter the amount to withdraw: "))
            if bank_account.withdraw(amount):
                print("Withdrawal successful")
            else:
                print("Insufficient balance or invalid amount")

        elif choice == 3:
            print(f"Your current balance: ${bank_account.balance}")

        elif choice == 4:
            print("Exiting...")
            break

        else:
            print("Invalid choice")

else:
    print("Login failed. Please check your account number and PIN.")