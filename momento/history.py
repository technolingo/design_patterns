
class BankAccountSnapshot:
    """
    A momento token class that captures a snapshot of a bank account's state.
    """

    def __init__(self, balance):
        self.balance = balance


class BankAccount:

    def __init__(self, balance=0):
        self.balance = balance
        self._changes = [BankAccountSnapshot(balance=self.balance)]
        self._current = 0

    def deposit(self, amount):
        self.balance += amount
        m = BankAccountSnapshot(balance=self.balance)
        self._changes.append(m)
        self._current += 1
        return m

    def withdraw(self, amount):
        self.balance -= amount
        m = BankAccountSnapshot(balance=self.balance)
        self._changes.append(m)
        self._current += 1
        return m

    def restore(self, snapshot):
        if snapshot:
            self.balance = snapshot.balance
            self._changes.append(snapshot)
            self._current = len(self._changes) - 1

    def undo(self):
        if self._current > 0:
            self._current -= 1
            m = self._changes[self._current]
            self.balance = m.balance
            return m

    def redo(self):
        if self._current + 1 < len(self._changes):
            self._current += 1
            m = self._changes[self._current]
            self.balance = m.balance
            return m

    def __repr__(self):
        return f'{self.__class__.__name__}(balance={self.balance})'


if __name__ == '__main__':
    acct = BankAccount()
    acct.deposit(200)
    acct.withdraw(50)
    print(acct)

    acct.undo()
    print(acct)

    acct.redo()
    print(acct)
