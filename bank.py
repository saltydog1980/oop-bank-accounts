import csv
import os

class Bank:
    def __init__(self, name):
        self.name = name
        # self.accounts = 

class Account:
    def __init__(self, id, balance, date_time):
        if int(balance) < 0:
            raise Exception("A new account cannot be created with a negative balance.")
        self.id = id
        self.balance = int(balance)
        self.date_time = date_time
        my_path = os.path.abspath(os.path.dirname(__file__))
        path = os.path.join(my_path, "support/account_owners.csv")
        fieldnames = ['id', 'user_id']
        with open(path) as csvfile:
            reader = csv.DictReader(csvfile, fieldnames)
            for row in reader:
                if row['id'] == self.id:
                    self.user_id = row['user_id']
        print(self.user_id)


    @classmethod
    def all_accounts(self):
        accounts = []
        my_path = os.path.abspath(os.path.dirname(__file__))
        path = os.path.join(my_path, "support/accounts.csv")
        fieldnames = ['id', 'balance', 'date_time']
        with open(path) as csvfile:
            reader = csv.DictReader(csvfile, fieldnames)
            for row in reader:
                accounts.append(Account(**dict(row)))
        return accounts
    
    @classmethod
    def find(self, id):
        my_path = os.path.abspath(os.path.dirname(__file__))
        path = os.path.join(my_path, "support/accounts.csv")
        fieldnames = ['id', 'balance', 'date_time']
        with open(path) as csvfile:
            reader = csv.DictReader(csvfile, fieldnames)
            for row in reader:
                if row['id'] == str(id):
                    return Account(**dict(row))

    def withdraw(self, amount):
        if self.balance - amount < 0:
            print("Insufficient funds for amount requested.")
        else:
            self.balance -= amount
            return self.balance
    
    def deposit(self, amount):
        self.balance += amount
        return self.balance

    def add_interst(self, rate):
        interest = (self.balance * rate) / 100
        self.balance += interest
        return interest

class SavingsAccount(Account):
    def __init__(self, id, balance, date_time):
        super().__init__(id, balance, date_time)
        if int(balance) < 10:
            raise ValueError("A new account cannot be created with less than $10.")

    def withdraw(self, amount):
        if self.balance - amount < 10:
            print("Cannot draw account below $10.")
        else:
            self.balance -= (amount + 2)
            return self.balance 

class CheckingAccount(Account):
    def __init__(self, id, balance, date_time):
        super().__init__(id, balance, date_time)
        self.check_count = 0

    def withdraw(self, amount):
        if self.balance - amount < 0:
            print("Insufficient funds.")
        else:
            self.balance -= (amount + 1)
            return self.balance
    
    def withdraw_using_check(self, amount):
        if self.balance - amount < -10:
            pass
        else:
            if self.check_count < 3:
                self.balance -= amount
                self.check_count += 1
                return self.balance
            else:
                self.balance -= (amount + 2)
                return self.balance

    def reset_checks(self):
        self.check_count = 0

class MoneyMarketAccount(Account):
    def __init__(self, id, balance, date_time):
        super().__init__(id, balance, date_time)
        if int(balance) < 10000:
            raise ValueError("A new account cannot be created with less than $10,000.")
        self.transaction_count = 0

    def withdraw(self, amount):
        if self.transaction_count == 6:
            print("Maximum transactions for the month have been reached.")
        else:
            if self.balance - amount < 10000:
                self.balance -= (amount + 100)
                self.transaction_count = 6
                return self.balance
            else:
                self.balance -= (amount)
                self.transaction_count += 1
                return self.balance

    def deposit(self, amount):
        if self.balance < 10000 and self.balance + amount > 10000:
            self.balance += amount
            return self.balance
        elif self.transaction_count == 6:
            print("Maximum transactions for the month have been reached.")
        else:
            self.balance += amount
            self.transaction_count += 1
            return self.balance

    def reset_transactions(self):
        self.transaction_count = 0

class Owners:
    def __init__(self, user_id, last_name, first_name, street_address, city, state):
        self.user_id = user_id
        self.last_name = last_name
        self.first_name = first_name
        self.street_address = street_address
        self.city = city
        self.state = state

    @classmethod
    def all_owners(self):
        owners = []
        my_path = os.path.abspath(os.path.dirname(__file__))
        path = os.path.join(my_path, "support/owners.csv")
        fieldnames = ['user_id', 'last_name', 'first_name', 'street_address', 'city', 'state']
        with open(path) as csvfile:
            reader = csv.DictReader(csvfile, fieldnames)
            for row in reader:
                owners.append(Owners(**dict(row)))

Account.all_accounts()
