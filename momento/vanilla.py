
class BankAccountSnapshot:
    """
    A momento token class that captures a snapshot of a bank account's state.
    """

    def __init__(self, balance):
        self.balance = balance


class BankAccount:

    def __init__(self, balance=0):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return BankAccountSnapshot(balance=self.balance)

    def withdraw(self, amount):
        self.balance -= amount
        return BankAccountSnapshot(balance=self.balance)

    def restore(self, snapshot):
        self.balance = snapshot.balance

    def __repr__(self):
        return f'{self.__class__.__name__}(balance={self.balance})'


if __name__ == '__main__':
    acct = BankAccount()
    m1 = acct.deposit(200)
    m2 = acct.withdraw(50)
    print(acct)

    acct.restore(m1)
    print(acct)
