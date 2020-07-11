def singleton(cls):
    instances = {}

    def get_instance(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]

    return get_instance


@singleton
class DBClient:

    def __init__(self, *args, **kwargs):
        print('__init__ is only called once')


db1 = DBClient()
db2 = DBClient()
print(db1)
print(db2)
print(db1 == db2)
