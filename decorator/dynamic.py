import os


class FileWithLogging:

    def __init__(self, file):
        self.file = file

    def writelines(self, strings):
        self.file.writelines(strings)
        print(f'Wrote {len(strings)} lines.')

    def __getattr__(self, key):
        return getattr(self.__dict__['file'], key)

    def __setattr__(self, key, val):
        if key == 'file':
            self.__dict__['file'] = val
        else:
            setattr(self.__dict__['file'], key, val)

    def __delattr__(self, key):
        if key == 'file':
            del self.__dict__['file']
        else:
            delattr(self.__dict__['file'], key)

    def __iter__(self):
        return self.file.__iter__()

    def __next__(self):
        return self.file.__next__()


if __name__ == "__main__":
    filepath = os.path.join(os.path.dirname(__file__), 'hello.txt')

    f = FileWithLogging(open(filepath, 'w'))
    f.writelines(['hello', 'world'])
    f.write('nihao')
    f.close()
