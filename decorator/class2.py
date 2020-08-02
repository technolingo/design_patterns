from abc import ABC


class Shape(ABC):

    def __str__(self):
        pass


class Circle(Shape):

    def __init__(self, radius):
        self.radius = radius

    def __str__(self):
        return f'Circle with radius of {self.radius}'


class ColouredShape(Shape):

    def __init__(self, shape, colour):
        self.shape = shape
        self.colour = colour

    def __str__(self):
        return f'{str(self.shape)} with colour {self.colour}'


if __name__ == "__main__":
    circle = Circle(2)
    red_circle = ColouredShape(circle, 'red')

    print(red_circle)
