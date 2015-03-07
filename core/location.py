from core.helpers import SelectionHelper


class Location:
    def __init__(self, name, description, directions, units, items):
        self.name = name
        self.description = description
        self.directions = directions

        self.directions_selector = SelectionHelper(self.directions)

        self.units_selector = SelectionHelper(units)
        self.units = units

        self.items = items
        self.items_selector = SelectionHelper(items)

    def kill_unit(self, unit):
        self.units.remove(unit)
        self.units_selector = SelectionHelper(self.units)

    def remove_item(self, item):
        self.items.remove(item)
        self.items_selector = SelectionHelper(self.items)


    def print(self):
        print(
            """
            ####################
            %s
            ####################
            %s
            """
            % (self.name, self.description)
        )
        print("You can go to(put location number):")

        self.directions_selector.print()


        if self.units:
            print("\nThere are(alive):")
            self.units_selector.print()
        print()

        if self.items:
            print("\nThere are some items:")
            self.items_selector.print()
        print()



