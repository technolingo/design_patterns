class DBClient:

    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls, *args, **kwargs)
        return cls._instance

    def __init__(self, *args, **kwargs):
        print('__init__ is called immediately after __new__')
        print('so this will not work flawlessly')


db1 = DBClient()
db2 = DBClient()
print(db1)
print(db2)
print(db1 == db2)
