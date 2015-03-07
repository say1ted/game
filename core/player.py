from core.creature import Creature
from core.inventory import Inventory
import random


class Player(Creature):
    def __init__(self, name, health, attack_min, attack_max, items):
        Creature.__init__(self, name, health, attack_min, attack_max, items)
        self.inventory = Inventory()

    def fight(self, unit):
        if bool(random.getrandbits(1)):
            print("Player make first strike")
            attacker = self
            defender = unit
        else:
            attacker = unit
            defender = self

        while self.is_alive() and unit.is_alive():
            self.__beat(attacker, defender)
            last_attacker = attacker
            attacker = defender
            defender = last_attacker

        if self.is_alive():
            print('{} have {} health'.format(self.name, self.health))
            print('{} lost'.format(unit.name))
            return True
        else:
            print('{} lost'.format(self.name))
            print('{} have {} health'.format(unit.name, unit.health))
            print("Game over!")
            return False


    def __beat(self, attacker, defenders):
        damage = random.randint(attacker.attack_min, attacker.attack_max)
        defenders.health = defenders.health - damage
        print('{} causes damage {} ( {} )'.\
              format(attacker.name, defenders.name, damage))