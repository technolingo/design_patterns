class Character:

    _intelligence = 0
    _stamina = 1
    _strength = 2

    def __init__(self):
        # list-backed properties
        self.stats = [25, 19, 20]

    @property
    def intelligence(self):
        return self.stats[self._intelligence]

    @property
    def stamina(self):
        return self.stats[self._stamina]

    @property
    def strength(self):
        return self.stats[self._strength]

    @property
    def sum_of_stats(self):
        return sum(self.stats)

    @property
    def max_of_stats(self):
        return max(self.stats)

    @property
    def avg_of_stats(self):
        return sum(self.stats) / len(self.stats)


if __name__ == "__main__":
    c = Character()
    print(c.intelligence)
    print(c.avg_of_stats)
