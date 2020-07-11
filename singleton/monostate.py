class Monostate:

    __shared_state = {}

    def __new__(cls, *args, **kwargs):
        obj = super().__new__(cls)
        obj.__dict__ = cls.__shared_state
        return obj


class DBClient(Monostate):

    def __init__(self, name, schema):
        self.name = name
        self.schema = schema

    def __repr__(self):
        return f'{self.name} - {self.schema}'


db1 = DBClient(name='app_db', schema='app_data')

print(db1)

db2 = DBClient(name='app_db', schema='new_schema')

print(db1)
print(db2)
