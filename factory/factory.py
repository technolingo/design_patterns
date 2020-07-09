from math import floor
from random import uniform


def get_coffee_discount():
    return uniform(0.1, 0.3)


class HotDrink:

    def __init__(self):
        self.name = None
        self.amount = None
        self.price = None

    def __str__(self):
        return f'This drink \'{self.name}\' contains {self.amount}ml, costs {self.price}EUR.'

    class HotDrinkFactory:

        def new_tea(self, name, amount, price):
            tea = HotDrink()
            tea.name = name
            tea.amount = amount
            tea.price = price
            return tea

        def new_coffee(self, name, amount, price):
            coffee = HotDrink()
            coffee.name = name
            coffee.amount = amount
            coffee.price = floor(price * (1 - get_coffee_discount()))
            return coffee

    factory = HotDrinkFactory()


tea = HotDrink.factory.new_tea('Capital T', 200, 4)
coffee = HotDrink.factory.new_coffee('Cappuccino', 400, 7)

print(tea)
print(coffee)
