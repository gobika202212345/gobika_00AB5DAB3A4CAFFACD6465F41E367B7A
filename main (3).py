class BankAccount:
    def __init__(self, account_number, account_holder_name, initial_balance):
        self.__account_number = account_number
        self.__account_holder_name = account_holder_name
        self.__account_balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.__account_balance += amount
            return f"Deposited ${amount}. New balance: ${self.__account_balance}"
        else:
            return "Invalid deposit amount. Please enter a positive number."

    def withdraw(self, amount):
        if amount > 0:
            if amount <= self.__account_balance:
                self.__account_balance -= amount
                return f"Withdrew ${amount}. New balance: ${self.__account_balance}"
            else:
                return "Insufficient funds."
        else:
            return "Invalid withdrawal amount. Please enter a positive number."

    def display_balance(self):
        return f"Account Balance for {self.__account_holder_name}: ${self.__account_balance}"

# Create an instance of the BankAccount class
account = BankAccount("12345", "John Doe", 1000.0)

# Test deposit functionality
print(account.deposit(500))  # Deposited $500. New balance: $1500.0

# Test withdrawal functionality
print(account.withdraw(200))  # Withdrew $200. New balance: $1300.0
print(account.withdraw(1500))  # Insufficient funds.

# Display account balance
print(account.display_balance())  # Account Balance for John Doe: $1300.0