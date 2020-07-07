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


class PersonBuilder:

    def __init__(self):
        self.person = Person()

    def build(self):
        return self.person


class PersonCompanyBuilder(PersonBuilder):

    def works_at(self, company):
        self.person.company = company
        return self


class PersonTitleBuilder(PersonCompanyBuilder):

    def as_a(self, title):
        self.person.title = title
        return self


class PersonIncomeBuilder(PersonTitleBuilder):

    def earning(self, income):
        self.person.income = income
        return self


class PersonAddressBuilder(PersonIncomeBuilder):

    def lives_at(self, address):
        self.person.address = address
        return self


class PersonPostcodeBuilder(PersonAddressBuilder):

    def with_postcode(self, postcode):
        self.person.postcode = postcode
        return self


class PersonCityBuilder(PersonPostcodeBuilder):

    def in_city(self, city):
        self.person.city = city
        return self


pb = PersonCityBuilder()

person = pb \
    .works_at('SpaceY') \
    .as_a('Engineer') \
    .earning(1000000) \
    .lives_at('42 Carl Sagan Street') \
    .with_postcode(12345) \
    .in_city('Marsian Colony') \
    .build()

print(person)
