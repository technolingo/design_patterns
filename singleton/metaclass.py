class Singleton(type):

    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(cls, *args, **kwargs)
        return cls._instances[cls]


class DBClient(metaclass=Singleton):

    def __init__(self, *args, **kwargs):
        print('__init__ is only called once')


db1 = DBClient()
db2 = DBClient()
print(db1)
print(db2)
print(db1 == db2)
