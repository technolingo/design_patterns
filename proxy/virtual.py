class Bitmap:

    def __init__(self, filename):
        self.filename = filename
        print(f'Loading image {filename}...')

    def render(self):
        print(f'Rendering image {self.filename}...')


class LazyBitmap:

    def __init__(self, filename):
        self.filename = filename
        self._bitmap = None

    def render(self):
        if self._bitmap is None:
            self._bitmap = Bitmap(self.filename)
        self._bitmap.render()


def render_image(image):
    print('Commencing rendering image...')
    image.render()
    print('Done rendering image.')


if __name__ == "__main__":
    bmp = LazyBitmap('wink.bmp')
    render_image(bmp)
