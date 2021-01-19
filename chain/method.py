class Creature:

    def __init__(self, name, health, attack):
        self.name = name
        self.health = health
        self.attack = attack

    def __str__(self):
        return f'Creature {self.name} with {self.health} health & {self.attack} attack.'


class CreatureModifier:

    def __init__(self, creature):
        self.creature = creature
        self.next_modifier = None

    def add(self, modifier):
        if self.next_modifier:
            self.next_modifier.add(modifier)
        else:
            self.next_modifier = modifier

    def apply(self):
        if self.next_modifier:
            self.next_modifier.apply()


class TakeDemageModifier(CreatureModifier):

    def apply(self):
        max_dmg = 10
        if self.creature.health - max_dmg > 0:
            print(f'{self.creature.name} is taking a demage of {max_dmg}...')
            self.creature.health -= max_dmg
        elif self.creature.health > 0:
            print(f'{self.creature.name} is killed.')
            self.creature.health = 0
        else:
            print(f'{self.creature.name} is dead.')
        super().apply()


class DoubleAttackModifier(CreatureModifier):

    def apply(self):
        print(f"Doubling {self.creature.name}'s attack...")
        self.creature.attack *= 2
        super().apply()


class DisableModifersModifer(CreatureModifier):

    def apply(self):
        print(f'All modifiers are disabled for {self.creature.name}.')


if __name__ == "__main__":
    creature = Creature('Hobbit', 200, 70)
    print(creature)

    rt_mod = CreatureModifier(creature)
    # rt_mod.add(DisableModifersModifer(creature))
    rt_mod.add(TakeDemageModifier(creature))
    rt_mod.add(DoubleAttackModifier(creature))
    rt_mod.add(TakeDemageModifier(creature))
    rt_mod.apply()

    print(creature)
