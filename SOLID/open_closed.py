# OCP: Open for Extension, Closed for Modification.

from abc import ABC, abstractmethod
from enum import Enum


class Colour:
    RED = 'red'
    GREEN = 'green'
    BLUE = 'blue'


class Size:
    SMALL = 'small'
    MEDIUM = 'medium'
    LARGE = 'large'


class Product:

    def __init__(self, name, colour, size):
        self.name = name
        self.colour = colour
        self.size = size

    def __str__(self):
        return f'A {self.size} {self.colour} {self.name}'


# This approach breaks the Open-Closed Principle and causes a State Space Explosion.
# class ProductFilter:

#     def filter_by_colour(self, products, colour):
#         return (p for p in products if p.colour == colour)

#     def filter_by_size(self, products, size):
#         return (p for p in products if p.size == size)

#     def filter_by_colour_and_size(self, products, colour, size):
#         return (p for p in products if p.colour == colour and p.size == size)

#     def filter_by_colour_or_size(self, products, colour, size):
#         return (p for p in products if p.colour == colour or p.size == size)


# The Specification Pattern
class SpecificationABC(ABC):

    @abstractmethod
    def is_satisfied(self, item):
        pass

    def __and__(self, other):
        return AndSpecification(self, other)

    # def __or__(self, other):
    #     return OrSpecification(self, other)


class FilterABC(ABC):

    @abstractmethod
    def filter(self, items, spec):
        pass


class ColourSpecification(SpecificationABC):

    def __init__(self, colour):
        self.colour = colour

    def is_satisfied(self, item):
        return item.colour == self.colour


class SizeSpecification(SpecificationABC):

    def __init__(self, size):
        self.size = size

    def is_satisfied(self, item):
        return item.size == self.size


class AndSpecification(SpecificationABC):

    def __init__(self, *args):
        self.args = args

    def is_satisfied(self, item):
        return all(map(
            lambda spec: spec.is_satisfied(item),
            self.args
        ))


class ProductFilter(FilterABC):

    def filter(self, items, spec):
        return (i for i in items if spec.is_satisfied(i))


if __name__ == '__main__':
    apple = Product('Apple', Colour.GREEN, Size.LARGE)
    grape = Product('Grape', Colour.BLUE, Size.SMALL)
    plum = Product('Plum', Colour.RED, Size.MEDIUM)

    products = [apple, grape, plum]
    pf = ProductFilter()

    green = ColourSpecification(Colour.GREEN)
    green_products = pf.filter(products, green)
    print([str(p) for p in green_products])

    large = SizeSpecification(Size.LARGE)
    large_products = pf.filter(products, large)
    print([str(p) for p in large_products])

    large_green = AndSpecification(large, green)
    large_green_products = pf.filter(products, large_green)
    print([str(p) for p in large_green_products])

    large_green = large & green  # overloading the binary & operator
    large_green_products = pf.filter(products, large_green)
    print([str(p) for p in large_green_products])
