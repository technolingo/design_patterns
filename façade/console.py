class Buffer:

    def __init__(self, capacity=100):
        self.__cursor = 0
        self.capacity = capacity
        self._buffer = [''] * capacity

    def __getitem__(self, key):
        return self._buffer.__getitem__(key)

    def append(self, val):
        self._buffer[self.__cursor] = val
        self.__cursor += 1
        if self.__cursor == self.capacity:
            self.__cursor = 0


class Viewport:

    def __init__(self, width=60, height=20, buffer=None):
        self.buffer = buffer if buffer else Buffer(width * height)
        self.offset = 0

    def read_char(self, idx):
        return self.buffer[self.offset + idx]

    def write_char(self, char):
        self.buffer.append(char)


class Console:

    def __init__(self):
        self.current_viewport = Viewport(width=60, height=20)
        self.viewports = [self.current_viewport]
        self.buffers = [self.current_viewport.buffer]

    def write(self, text):
        for char in text:
            self.current_viewport.write_char(char)

    def read(self):
        return ''.join(self.current_viewport.buffer)

    def read_char(self, idx):
        return self.current_viewport.read_char(idx)


if __name__ == '__main__':
    console = Console()
    console.write('hello!')
    print(console.read())
