"""
A contrived and convoluted example of a classic implementation of the state pattern.
"""

from abc import ABC


class StateABC(ABC):

    def on(self, switch):
        print('Light is already on.')

    def off(self, switch):
        print('Light is already off.')


class OnState(StateABC):

    def __init__(self):
        print('Light is turned on.')

    def off(self, switch):
        print('Turning light off.')
        switch.state = OffState()


class OffState(StateABC):

    def __init__(self):
        print('Light is turned off.')

    def on(self, switch):
        print('Turning light on.')
        switch.state = OnState()


class Switch:

    def __init__(self):
        self.state = OffState()

    def on(self):
        self.state.on(self)

    def off(self):
        self.state.off(self)


if __name__ == '__main__':
    sw = Switch()
    sw.on()
    sw.off()
    sw.off()
