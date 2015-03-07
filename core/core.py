import sys
from core.helpers import SelectionHelper

class Core():
    def __init__(self, builder):
        self.print()
        self.builder = builder
        self.player = self.builder.get_player()
        self.go('Forest')

    #TODO: Сделать единообразно, а то гдето имя передается а где-то сам обьект
    def go(self, location_name):
        self.current_location = self.builder.get_location(location_name)
        self.current_location.print()

    def attack(self, unit):
        if not self.player.fight(unit):
            sys.exit(0)

        self.current_location.kill_unit(unit)
        self.current_location.items.extend(unit.items)
        self.current_location.items_selector = SelectionHelper(self.current_location.items)

    def info(self):
        self.current_location.print()

    # Inventory functions
    def inventory(self):
        self.player.inventory.print()

    def drop(self, item):
        self.player.inventory.drop(item)
        self.current_location.items.append(item)
        self.current_location.items_selector = SelectionHelper(self.current_location.items)

    def take(self, item):
        self.player.inventory.take(item)
        self.current_location.remove_item(item)


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


