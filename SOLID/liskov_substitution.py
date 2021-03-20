"""
The Liskov Substitution Principle imperates that objects of a superclass shall be replaceable
with objects of its subclasses without breaking the application. In other words,
the objects of the subclasses should behave in the same way as the objects of their superclass.
"""


class Rectangle:

    def __init__(self, width, height):
        self._height = height
        self._width = width

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        self._width = value

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        self._height = value

    @property
    def area(self):
        return self._width * self._height

    def __str__(self):
        return f'Width: {self.width}, height: {self.height}'


def calculate_area(rc):
    """
    As an anti-pattern, this function only works on Rectangle and not on derived classes.
    """
    w = rc.width
    rc.height = 10
    expected = w * 10
    print(f'Expected an area of {expected}, got {rc.area}')


class Square(Rectangle):

    def __init__(self, size):
        super().__init__(size, size)

    @Rectangle.width.setter  # pylint: disable=no-member
    def width(self, value):
        self._width = self._height = value

    @Rectangle.height.setter  # pylint: disable=no-member
    def height(self, value):
        self._height = self._width = value


rc = Rectangle(2, 3)
calculate_area(rc)

sq = Square(5)
calculate_area(sq)
