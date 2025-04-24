from abc import ABC, abstractmethod

class BankAccount(ABC):
    def __init__(self, account_number, balance=0):
        self.__account_number = account_number
        self.__balance = balance

    @property
    def account_number(self):
        return self.__account_number

    @property
    def balance(self):
        return self.__balance

    def _set_balance(self, amount):
        self.__balance = amount

    @abstractmethod
    def deposit(self, amount):
        pass

    @abstractmethod
    def withdraw(self, amount):
        pass

    @abstractmethod
    def display_account_type(self):
        pass


class CurrentAccount(BankAccount):
    OVERDRAFT_LIMIT = -5000

    def deposit(self, amount):
        if amount > 0 and (self.balance - amount) >= self.OVERDRAFT_LIMIT:
            self._set_balance(self.balance + amount)
            return True
        return False

    def withdraw(self, amount):
        if amount > 0 and (self.balance - amount) >= self.OVERDRAFT_LIMIT:
            self._set_balance(self.balance - amount)
            return True
        return False

    def display_account_type(self):
        return "Current Account"


class SavingsAccount(BankAccount):
    def deposit(self, amount):
        if amount > 0:
            self._set_balance(self.balance + amount)
            return True
        return False

    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self._set_balance(self.balance - amount)
            return True
        return False

    def display_account_type(self):
        return f"Savings Account: {self.balance}"


def print_account_details(account):
    print(f"Account Number: {account.account_number}")
    print(f"Balance: {account.balance}")
    print(f"Account Type: {account.display_account_type()}")
    print("-" * 40)


if __name__ == "__main__":
    saving_acc1 = SavingsAccount("SA12345", 2000)
    current_acc1 = CurrentAccount("CA456", 0)
    saving_acc2 = SavingsAccount("Keni0220", 2000)
    current_acc2 = CurrentAccount("Zai2200", 0)


    current_acc1.deposit(1000)
    current_acc1.withdraw(1200)
    saving_acc1.deposit(2000)
    saving_acc1.withdraw(3000)
    current_acc2.deposit(1000)
    current_acc2.withdraw(1200)
    saving_acc2.deposit(2000)
    saving_acc2.withdraw(3000)


    print_account_details(saving_acc1)
    print_account_details(current_acc1)
    print_account_details(saving_acc2)
    print_account_details(current_acc2)

