"""
An intrusive visitor achieves some functionality by augmenting components of a hierachy,
but breaks the open-closed principle. e.g. `print` & `eval` methods below:
"""


class AdditionExpression:

    def __init__(self, left, right):
        self.left = left
        self.right = right

    def print(self, buffer):
        buffer.append('(')
        self.left.print(buffer)
        buffer.append('+')
        self.right.print(buffer)
        buffer.append(')')

    def eval(self):
        return self.left.eval() + self.right.eval()


class DoubleExpression:

    def __init__(self, value):
        self.value = value

    def print(self, buffer):
        buffer.append(str(self.value))

    def eval(self):
        return self.value


if __name__ == '__main__':
    e = AdditionExpression(
        DoubleExpression(1),
        AdditionExpression(
            DoubleExpression(2),
            DoubleExpression(3)
        )
    )

    buffer = []
    e.print(buffer)
    print(''.join(buffer), '=', e.eval())
