"""
A reflective visitor checks the type of the target object and performs the intended
functionality accordingly.

The downside is that the visitor will fail silently if more members are introduced into
the hierachy if the visitor is not manually updated along with the new member.
"""

from abc import ABC


class Expression(ABC):
    pass


class AdditionExpression(Expression):

    def __init__(self, left, right):
        self.left = left
        self.right = right


class DoubleExpression(Expression):

    def __init__(self, value):
        self.value = value


class ExpressionPrinter:

    @classmethod
    def print(cls, exp, buffer):
        if isinstance(exp, AdditionExpression):
            buffer.append('(')
            cls.print(exp.left, buffer)
            buffer.append('+')
            cls.print(exp.right, buffer)
            buffer.append(')')
        elif isinstance(exp, DoubleExpression):
            buffer.append(str(exp.value))


# Bind the visitor method to members of the hierachy
Expression.print = lambda self, buffer: ExpressionPrinter.print(self, buffer)


if __name__ == '__main__':
    e = AdditionExpression(
        DoubleExpression(1),
        AdditionExpression(
            DoubleExpression(2),
            DoubleExpression(3)
        )
    )

    buffer = []
    # ExpressionPrinter.print(e, buffer)
    e.print(buffer)
    print(''.join(buffer))
