from copy import deepcopy


class Address:

    def __init__(self, office_num, street_addr, city):
        self.office_num = office_num
        self.street_addr = street_addr
        self.city = city

    def __str__(self):
        return f'{self.street_addr}, {self.city} (Office {self.office_num})'


class Employee:

    def __init__(self, name, address):
        self.name = name
        self.address = address

    def __str__(self):
        return f'{self.name} works at {self.address}.'


class EmployeeFactory:

    main_office_employee = Employee('', Address(0, '123 Central Ave.', 'Berlin'))
    aux_office_employee = Employee('', Address(0, '456 Baker St.', 'Berlin'))

    @staticmethod
    def __new_employee(proto, name, office_num):
        employee = deepcopy(proto)
        employee.name = name
        employee.address.office_num = office_num
        return employee

    @classmethod
    def new_main_office_employee(cls, name, office_num):
        return cls.__new_employee(cls.main_office_employee, name, office_num)

    @classmethod
    def new_aux_office_employee(cls, name, office_num):
        return cls.__new_employee(cls.aux_office_employee, name, office_num)


e1 = EmployeeFactory.new_main_office_employee('Jane', 23)
e2 = EmployeeFactory.new_aux_office_employee('John', 17)
print(e1)
print(e2)
