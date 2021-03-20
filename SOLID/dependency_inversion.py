from abc import abstractmethod
from enum import Enum, auto


class Relationship:
    PARENT = auto()
    CHILD = auto()
    SIBLING = auto()


class Person:

    def __init__(self, name):
        self.name = name


class RelationshipBrowser:

    @abstractmethod
    def find_children(self, parent):
        raise NotImplementedError


class Relationships(RelationshipBrowser):
    """
    A low-level module.
    """

    def __init__(self):
        self.relations = []

    def add_parent_child_relation(self, parent, child):
        self.relations.append((parent, Relationship.PARENT, child))
        self.relations.append((child, Relationship.CHILD, parent))

    def find_children(self, parent):
        return (r[2] for r in self.relations if r[0] == parent and r[1] == Relationship.PARENT)


class Research:
    """
    A high-level module.
    """

    def __init__(self, relationships):
        self.relationships = relationships

    # def find_all_children_of(self, parent):
        # we shouldn't access the implementation details of low-level modules in high-level modules
        # viz. The high-level module `Research` shouldn't depend on the internal storage mechanism
        # `relations` of the low-level module `Relationship`
        # Since if the low-level implementation changes, the high-level code will break
    #     for r in self.relationships.relations:
    #         if r[0].name == parent.name and r[1] == Relationship.PARENT:
    #             print(f'{parent.name} has a child called {r[2].name}.')

    def find_all_children_of(self, parent):
        for c in self.relationships.find_children(parent):
            print(f'{parent.name} has a child called {c.name}.')


parent = Person('John')
child1 = Person('Julia')
child2 = Person('Jessica')

relationships = Relationships()
relationships.add_parent_child_relation(parent, child1)
relationships.add_parent_child_relation(parent, child2)

research = Research(relationships)
research.find_all_children_of(parent)
