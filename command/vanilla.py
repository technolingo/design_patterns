from abc import ABC, abstractmethod
from enum import Enum


class BankAccount:

    def __init__(self, balance=0, overdraft_limit=-500):
        self.balance = balance
        self.overdraft_limit = overdraft_limit

    def deposit(self, amount):
        if amount <= 0:
            return False
        self.balance += amount
        print(f'Deposited {amount}. New balance: {self.balance}.')
        return True

    def withdraw(self, amount):
        if amount <= 0:
            return False
        if self.balance - amount >= self.overdraft_limit:
            self.balance -= amount
            print(f'Withdrew {amount}. New balance: {self.balance}.')
            return True

        print(f'Insufficient funds. Balance: {self.balance}.')
        return False

    def __str__(self):
        return f'{self.__class__.__name__}(' \
            f'balance={self.balance}, overdraft_limit={self.overdraft_limit})'


class Command(ABC):
    """
    A command interface that allows transactions to be executed and reverted.
    """

    @abstractmethod
    def invoke(self):
        pass

    @abstractmethod
    def undo(self):
        pass


class BankAccountCommand(Command):

    class Action(Enum):

        DEPOSIT = 'DEPOSIT'
        WITHDRAW = 'WITHDRAW'

    def __init__(self, account, action, amount):
        self.account = account
        self.action = action
        self.amount = amount
        self._success = None

    def invoke(self):
        if self.action == self.Action.DEPOSIT:
            self._success = self.account.deposit(self.amount)
        elif self.action == self.Action.WITHDRAW:
            self._success = self.account.withdraw(self.amount)

    def undo(self):
        if not self._success:
            return
        if self.action == self.Action.DEPOSIT:
            self.account.withdraw(self.amount)
        elif self.action == self.Action.WITHDRAW:
            self.account.deposit(self.amount)


if __name__ == "__main__":
    acc = BankAccount(balance=100)
    cmd = BankAccountCommand(acc, BankAccountCommand.Action.DEPOSIT, 50.67)
    cmd.invoke()
    print(acc)
    cmd.undo()
    print(acc)
