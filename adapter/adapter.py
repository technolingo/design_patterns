class Cat:

    def __init__(self, name):
        self.name = name
        self.kind = 'Cat'

    def meow(self):
        return 'meow'

    def purr(self):
        return 'rrrrrrr'


class Dog:

    def __init__(self):
        self.kind = 'Dog'

    def bark(self):
        return 'woof'


class Human:

    def __init__(self):
        self.kind = 'Human'

    def speak(self):
        return 'hello'


class Adapter:

    def __init__(self, obj, **methods):
        self.obj = obj
        self.__dict__.update(methods)

    def __getattr__(self, attr):
        return getattr(self.obj, attr)


objects = []

cat = Cat(name='Ser Pounce')
objects.append(Adapter(cat, greet=cat.meow))

dog = Dog()
objects.append(Adapter(dog, greet=dog.bark))

human = Human()
objects.append(Adapter(human, greet=human.speak))

for obj in objects:
    print(f'{obj.kind}: {obj.greet()}!')
