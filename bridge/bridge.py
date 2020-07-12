# Cartesian Product Complexity Explosion
# - decouple multiple hierachies
# circle square
# vector raster

from abc import ABC


class Renderer(ABC):

    def render_circle(self, radius):
        pass

    def render_square(self, side):
        pass


class VectorRenderer(Renderer):

    def render_circle(self, radius):
        print(f'Rendering a vector circle of radius {radius}')

    def render_square(self, side):
        print(f'Rendering a vector square of side {side}')


class RasterRenderer(Renderer):

    def render_circle(self, radius):
        print(f'Rendering a raster circle of radius {radius}')

    def render_square(self, side):
        print(f'Rendering a raster square of side {side}')


class Shape(ABC):

    def __init__(self, renderer):
        self.renderer = renderer

    def draw(self):
        pass

    def resize(self, factor):
        pass


class Circle(Shape):

    def __init__(self, renderer, radius):
        super().__init__(renderer)
        self.radius = radius

    def draw(self):
        return self.renderer.render_circle(self.radius)

    def resize(self, factor):
        self.radius *= factor


class Square(Shape):

    def __init__(self, renderer, side):
        super().__init__(renderer)
        self.side = side

    def draw(self):
        return self.renderer.render_square(self.side)

    def resize(self, factor):
        self.side *= factor


vector = VectorRenderer()
raster = RasterRenderer()

vector_circle = Circle(vector, 5)
vector_circle.draw()
vector_circle.resize(factor=2)
vector_circle.draw()

raster_square = Square(raster, 5)
raster_square.draw()
