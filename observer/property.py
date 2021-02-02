class Event(list):
    """
    A composite event type that holds an array of observers as well as events.
    """

    def __call__(self, *args, **kwargs):
        for item in self:
            item(*args, **kwargs)


class PropertyObservableMixin:
    """
    A mixin class that enables observable objects to publish changes on their properties.
    """

    def __init__(self):
        self.property_changed = Event()


class Person(PropertyObservableMixin):
    """
    An observable class that generates property changed events.
    """

    def __init__(self, age=0):
        super().__init__()
        self._age = age

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        if value == self._age:
            return self._age

        self._age = value
        self.property_changed('age', value)


class TrafficAuthority:
    """
    An observer class that subscribes to events.
    """

    def __init__(self, person):
        self.person = person
        person.property_changed.append(self.person_changed)

    def person_changed(self, name, value):
        if name == 'age':
            if value < 18:
                print('You still cannot drive.')
            else:
                print('You can drive now.')
                self.person.property_changed.remove(self.person_changed)


if __name__ == '__main__':
    p = Person()
    ta = TrafficAuthority(p)

    p.age = 14
    p.age = 16
    p.age = 20
    p.age = 24


# NOTE: The property observer pattern is only suitable when properties are independent of each
# other; otherwise it becomes difficult to maintain and scale.
