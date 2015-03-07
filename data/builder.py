import json, os
from core.location import Location
from core.creature import Creature
from core.unit import Unit
from core.player import Player
from core.item import Item


class Builder():

    def __init__(self, data_path='data'):
        self.data_path = data_path

    def get_creatures(self):
        data = self.__get_data('units.json')
        creatures = []

        #TODO:У плеера лишний items
        for creature_name, creature_data in data.items():
            health = creature_data['Health']
            attacks = creature_data['Attack'].split('-')
            attack_min = int(attacks[0])
            attack_max = int(attacks[1])
            items = []

            if 'Items' in creature_data:
                for item_name in creature_data['Items']:
                    items.append(self.get_item(item_name))

            creatures.append(Creature(creature_name, health, attack_min, attack_max, items))

        return creatures

    def get_locations(self):
        data = self.__get_data('locations.json')
        locations = []

        for location_name, location_data in data.items():
            description = location_data['Description']
            directions = location_data['Directions']

            units = []
            if 'Units' in location_data:
                for unit_name in location_data['Units']:
                    units.append(self.get_unit(unit_name))

            items = []
            if 'Items' in location_data:
                for item_name in location_data['Items']:
                    items.append(self.get_item(item_name))
            locations.append(Location(location_name, description, directions, units, items))

        return locations

    def __get_data(self, filename):
         with open(os.path.join(self.data_path, filename ), 'r') as data_file:
            return json.load(data_file)

    def get_unit(self, name):
        for creature in self.get_creatures():
            if creature.name == name:
                return Unit(creature.name, creature.health, creature.attack_min, creature.attack_max, creature.items)

    def get_player(self):
        for creature in self.get_creatures():
            if creature.name == 'Player':
                return Player(creature.name, creature.health, creature.attack_min, creature.attack_max, [])

    def get_location(self, name):
        for location in self.get_locations():
            if location.name == name:
                return location

    def get_item(self, name):
        for item in self.get_items():
            if item.name == name:
                return item

    def get_items(self):
        data = self.__get_data('items.json')
        items = []

        for item_name, item_data in data.items():
            items.append(Item(item_name, item_data['Description']))

        return items

#TODO: сделать преобразование типов в get_player и get_unit
#TODO: много одинаковых действий
#TODO: сложно протестировать
