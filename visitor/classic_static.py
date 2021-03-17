"""
The classic visitor implementation uses an `accept` method on the host hierachy to supply the
visitor with the current type and a decorator on top of the visitor methods that checks the type
of the target object and redirects to the corresponding `visit` method, hence "double despatch".

The `accept` method is required for statically typed languages.
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


class Expression(ABC):

    def accept(self, visit):
        visit.visit(self)


class AdditionExpression(Expression):

    def __init__(self, left, right):
        self.left = left
        self.right = right


class DoubleExpression(Expression):

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
        exp.left.accept(self)
        self._buffer.append('+')
        exp.right.accept(self)
        self._buffer.append(')')

    def __str__(self):
        return ''.join(self._buffer)


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
    print(expptr)
