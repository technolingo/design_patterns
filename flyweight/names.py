class User:

    _names = []

    def __init__(self, fullname):
        self.fullname = fullname
        self._fullname_indices = None

    @property
    def fullname(self):
        return ' '.join([self._names[self._fullname_indices[0]],
                         self._names[self._fullname_indices[1]]])

    @fullname.setter
    def fullname(self, val):
        def get_or_add(name):
            if name in self._names:
                return self._names.index(name)
            else:
                self._names.append(name)
                return len(self._names) - 1
        self._fullname_indices = [get_or_add(n) for n in self.fullname.split(' ')]

    def __str__(self):
        return self.fullname
