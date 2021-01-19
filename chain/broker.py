# Event Broker
# Command Query Separation (CQS)

from abc import ABC, abstractmethod
from enum import Enum


class Event(list):

    def __call__(self, *args, **kwargs):
        for item in self:
            item(*args, **kwargs)


class QueryType(Enum):

    HEALTH = 'HEALTH'
    ATTACK = 'ATTACK'


class Query:

    def __init__(self, creature_name, query_type, default_value):
        self.creature_name = creature_name
        self.query_type = query_type
        self.value = default_value


class Game:
    """
    A centralised event broker that handles queries to a creature's stats in real time.
    """

    def __init__(self):
        self.queries = Event()

    def execute(self, sender, query):
        self.queries(sender, query)


class Creature:
    def __init__(self, game, name, health, attack):
        self.name = name
        self.game = game
        self.initial_health = health
        self.initial_attack = attack

    @property
    def health(self):
        q = Query(self.name, QueryType.HEALTH, self.initial_health)
        self.game.execute(self, q)
        return q.value

    @property
    def attack(self):
        q = Query(self.name, QueryType.ATTACK, self.initial_attack)
        self.game.execute(self, q)
        return q.value

    def __str__(self):
        return f'Creature {self.name} with {self.health} health & {self.attack} attack.'


class CreatureModifier(ABC):

    def __init__(self, game, creature):
        self.game = game
        self.creature = creature
        self.game.queries.append(self.apply)

    @abstractmethod
    def apply(self, sender, query):
        pass

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.game.queries.remove(self.apply)


class TakeDemageModifier(CreatureModifier):

    def apply(self, sender, query):
        if sender.name == self.creature.name and query.query_type == QueryType.HEALTH:
            max_dmg = 10
            if query.value - max_dmg > 0:
                query.value -= max_dmg
            elif query.value > 0:
                query.value = 0


class DoubleAttackModifier(CreatureModifier):

    def apply(self, sender, query):
        if sender.name == self.creature.name and query.query_type == QueryType.ATTACK:
            query.value *= 2


if __name__ == '__main__':
    game = Game()
    creature = Creature(game, 'Hobbit', 200, 70)
    print(creature)

    with DoubleAttackModifier(game, creature):
        print(creature)
        with TakeDemageModifier(game, creature):
            print(creature)

    print(creature)
