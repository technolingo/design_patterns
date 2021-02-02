class Event(list):
    """
    A composite event type that holds an array of observers as well as events.
    """

    def __call__(self, *args, **kwargs):
        for item in self:
            item(*args, **kwargs)


class Patient:
    """
    An observable class that represents patients who generate medical events.
    """

    def __init__(self, name, addr):
        self.name = name
        self.addr = addr
        self.event = Event()

    def get_sick(self):
        self.event(self.name, self.addr)


def arrange_doctor(name, addr):
    """
    An observer function that processes individual events.
    """
    print(f'Arranging a doctor for {name} at {addr}...')


if __name__ == '__main__':
    p = Patient('John', '21 Central Av.')
    p.event.append(lambda name, addr: print(f'{name} at {addr} is ill.'))
    p.event.append(arrange_doctor)

    p.get_sick()

    print('---')
    p.event.remove(arrange_doctor)
    p.get_sick()
