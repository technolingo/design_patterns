"""
This alternative implementation of the visitor pattern uses duck typing to simplify
the classic 'double despatch' implementation and removes the `accept` method.
"""

from abc import ABC


# ↓↓↓ LIBRARY CODE ↓↓↓
# taken from https://tavianator.com/the-visitor-pattern-in-python/

# Stores the actual visitor methods
_methods = {}


def _qualname(obj):
    """Get the fully-qualified name of an object (including module)."""
    return obj.__module__ + '.' + obj.__qualname__


def _declaring_class(obj):
    """Get the name of the class that declared an object."""
    name = _qualname(obj)
    return name[:name.rfind('.')]


def _visitor_impl(self, arg):
    """Actual visitor method implementation."""
    method = _methods[(_qualname(type(self)), type(arg))]
    return method(self, arg)


def visitor(arg_type):
    """Decorator that creates a visitor method."""

    def decorator(fn):
        declaring_class = _declaring_class(fn)
        _methods[(declaring_class, arg_type)] = fn

        # Replace all decorated methods with _visitor_impl
        return _visitor_impl

    return decorator

# ↑↑↑ LIBRARY CODE ↑↑↑


class AdditionExpression:

    def __init__(self, left, right):
        self.left = left
        self.right = right


class DoubleExpression:

    def __init__(self, value):
        self.value = value


class ExpressionPrinter:

    def __init__(self):
        self._buffer = []

    @visitor(arg_type=DoubleExpression)
    def visit(self, exp):
        self._buffer.append(str(exp.value))

    @visitor(arg_type=AdditionExpression)
    def visit(self, exp):  # pylint: disable=function-redefined
        self._buffer.append('(')
        self.visit(exp.left)
        self._buffer.append('+')
        self.visit(exp.right)
        self._buffer.append(')')

    def __str__(self):
        return ''.join(self._buffer)


class ExpressionEvaluator:

    def __init__(self):
        self.value = None

    @visitor(arg_type=DoubleExpression)
    def visit(self, exp):
        self.value = exp.value

    @visitor(arg_type=AdditionExpression)
    def visit(self, exp):  # pylint: disable=function-redefined
        self.visit(exp.left)
        # must cache the state here
        val = self.value
        self.visit(exp.right)
        self.value += val

    def __str__(self):
        return str(self.value)


if __name__ == '__main__':
    e = AdditionExpression(
        DoubleExpression(1),
        AdditionExpression(
            DoubleExpression(2),
            DoubleExpression(3)
        )
    )

    expptr = ExpressionPrinter()
    expptr.visit(e)

    expevl = ExpressionEvaluator()
    expevl.visit(e)

    # (1+(2+3)) = 6
    print(expptr, '=', expevl)
