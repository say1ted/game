from core.player import Player
from core.location import Location
from core.unit import Unit
from shell import UserShell
import sys


class Core():
    def __init__(self):
        self.print()
        first_location_name = 'Forest'
        self.player = Player('Player')
        self.go(first_location_name)

    def go(self, location_name):
        self.current_location = Location(location_name)

    def attack(self, unit_name):
        unit = Unit(unit_name)
        if not self.player.fight(unit):
            sys.exit(0)


    def print(self):
        print(
        """
        @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
        @ Hello! Today you will be a hero @
        @ A hero in Middle Ages. You sho- @
        @ uld be attentive and help girls @
        @ Be lucky.                       @
        @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
        """)

if __name__ == '__main__':
    core = Core()
    shell = UserShell()
    shell.set_core(core)
    shell.cmdloop()
