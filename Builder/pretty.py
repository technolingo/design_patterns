class Person:

    def __init__(self):
        self.company = None
        self.title = None
        self.income = None
        self.address = None
        self.postcode = None
        self.city = None

    def __repr__(self):
        return f'{self.__class__.__name__}(company={self.company}, ' \
            f'title={self.title}, income={self.income}, address={self.address}, ' \
            f'postcode={self.postcode}, city={self.city})'

    @staticmethod
    def new():
        return PersonBuilder()


class PersonBuilder:

    def __init__(self, person=Person()):
        self.person = person

    @property
    def works(self):
        return PersonJobBuilder(self.person)

    @property
    def lives(self):
        return PersonHomeBuilder(self.person)

    def build(self):
        return self.person


class PersonJobBuilder(PersonBuilder):

    def __init__(self, person):
        super().__init__(person)

    def at(self, company):
        self.person.company = company
        return self

    def as_a(self, title):
        self.person.title = title
        return self

    def earning(self, income):
        self.person.income = income
        return self


class PersonHomeBuilder(PersonBuilder):

    def __init__(self, person):
        super().__init__(person)

    def at(self, address):
        self.person.address = address
        return self

    def with_postcode(self, postcode):
        self.person.postcode = postcode
        return self

    def in_city(self, city):
        self.person.city = city
        return self


person = Person.new() \
    .works \
    .at('SpaceY') \
    .as_a('Engineer') \
    .earning(1000000) \
    .lives \
    .at('42 Carl Sagan Street') \
    .with_postcode(12345) \
    .in_city('Marsian Colony') \
    .build()

print(person)
