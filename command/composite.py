import unittest
from enum import Enum
from abc import ABC, abstractmethod


class BankAccount:

    def __init__(self, balance=0, overdraft_limit=-500):
        self.balance = balance
        self.overdraft_limit = overdraft_limit

    def deposit(self, amount):
        if amount <= 0:
            return False
        self.balance += amount
        return True

    def withdraw(self, amount):
        if amount <= 0:
            return False
        if self.balance - amount >= self.overdraft_limit:
            self.balance -= amount
            return True
        return False

    def __str__(self):
        return f'{self.__class__.__name__}(' \
            f'balance={self.balance}, overdraft_limit={self.overdraft_limit})'


class Command(ABC):
    """
    A command interface that allows transactions to be executed and reverted.
    """

    def __init__(self):
        self.success = False

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
        super().__init__()
        self.account = account
        self.action = action
        self.amount = amount

    def invoke(self):
        if self.action == self.Action.DEPOSIT:
            self.success = self.account.deposit(self.amount)
        elif self.action == self.Action.WITHDRAW:
            self.success = self.account.withdraw(self.amount)

    def undo(self):
        if not self.success:
            return
        if self.action == self.Action.DEPOSIT:
            self.account.withdraw(self.amount)
        elif self.action == self.Action.WITHDRAW:
            self.account.deposit(self.amount)


class CompositeBankAccountCommand(Command, list):
    """
    A composite command interface that behaves as both a command and a list of commands.
    """

    def __init__(self, items=[]):
        super().__init__()
        for i in items:
            self.append(i)

    def invoke(self):
        for i in self:
            i.invoke()

    def undo(self):
        for i in reversed(self):
            i.undo()


class MoneyTransferCommand(CompositeBankAccountCommand):

    def __init__(self, from_acct, to_acct, amount):
        super().__init__(items=[
            BankAccountCommand(from_acct, BankAccountCommand.Action.WITHDRAW, amount),
            BankAccountCommand(to_acct, BankAccountCommand.Action.DEPOSIT, amount)
        ])

    def invoke(self):
        ok = True
        for cmd in self:
            if ok:
                cmd.invoke()
                ok = cmd.success
            else:
                cmd.success = False
        self.success = ok


class TestSuite(unittest.TestCase):

    def test_composite_deposit(self):
        acc = BankAccount(balance=10)
        dep1 = BankAccountCommand(acc, BankAccountCommand.Action.DEPOSIT, 50)
        dep2 = BankAccountCommand(acc, BankAccountCommand.Action.DEPOSIT, 20)
        composite = CompositeBankAccountCommand(items=[dep1, dep2])
        composite.invoke()
        assert acc.balance == 80
        composite.undo()
        assert acc.balance == 10

    def test_transfer_ok(self):
        acc1 = BankAccount(balance=200)
        acc2 = BankAccount(balance=10)
        cmd = MoneyTransferCommand(acc1, acc2, 70)
        cmd.invoke()
        assert acc1.balance == 130
        assert acc2.balance == 80
        cmd.undo()
        assert acc1.balance == 200
        assert acc2.balance == 10

    def test_transfer_ko(self):
        acc1 = BankAccount(balance=200)
        acc2 = BankAccount(balance=10)
        cmd = MoneyTransferCommand(acc1, acc2, 1000)
        cmd.invoke()
        assert acc1.balance == 200
        assert acc2.balance == 10
        cmd.undo()
        assert acc1.balance == 200
        assert acc2.balance == 10


if __name__ == "__main__":
    unittest.main()
