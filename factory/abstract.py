from abc import ABC
from enum import Enum


class HotDrink(ABC):

    def consume(self):
        pass


class Tea(HotDrink):

    def consume(self):
        print('Drinking tea...')


class Coffee(HotDrink):

    def consume(self):
        print('Drinking coffee...')


class HotDrinkFactory(ABC):

    def prepare(self):
        pass


class TeaFactory(HotDrinkFactory):

    def prepare(self, amount):
        print(f'Preparing {amount}ml of tea...')
        return Tea()


class CoffeeFactory(HotDrinkFactory):

    def prepare(self, amount):
        print(f'Preparing {amount}ml of coffee...')
        return Coffee()


class HotDrinkMachine:

    class AvailableHotDrinks(Enum):
        TEA = 1
        COFFEE = 2

    factories = []
    initialized = False

    def __init__(self):
        if not self.initialized:
            self.initialized = True
            for drink in self.AvailableHotDrinks:
                name = drink.name.capitalize()
                factory_name = name + 'Factory'
                factory_instance = eval(factory_name)()
                self.factories.append((name, factory_instance))

    def receive_order(self):
        print('Available drinks:')
        cnt = -1
        for factory in self.factories:
            cnt += 1
            print(cnt, factory[0])

        idx = input(f'Please order a drink (0~{cnt}): ')
        amt = input('Please specify amount (ml): ')
        return self.factories[int(idx)][1].prepare(amt)


if __name__ == "__main__":
    hdm = HotDrinkMachine()
    hdm.receive_order()
