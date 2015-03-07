from unittest import TestCase
from core.core import Core
from data.builder import Builder
from core.player import Player
from core.unit import Unit
from core.location import Location
from core.item import Item


class TestCore(TestCase):
    def setUp(self):
        self.core = Core(Builder('../data'))

    def test_go(self):
        self.core.go('Home')
        self.assertTrue(self.core.current_location.name == 'Home')

    def test_attack(self):
        unit = self.core.current_location.units[0]
        self.core.attack(unit)
        result = unit in self.core.current_location.units
        self.assertFalse(result)

    def test_take(self):
        self.core.go('Lake')
        item = self.core.current_location.items[0]
        self.core.take(item)
        self.assertFalse(item in self.core.current_location.items)
        self.assertTrue(item in self.core.player.inventory.items)

    def test_drop(self):
        self.core.go('Lake')
        item = self.core.current_location.items[0]
        self.core.take(item)
        self.assertTrue(item in self.core.player.inventory.items)
        self.core.drop(item)
        self.assertFalse(item in self.core.player.inventory.items)
        self.assertTrue(item in self.core.current_location.items)

    def test_drop_item_from_unit(self):
        unit = Unit("Goblin", 10, 1, 1, ["Axe"])
        item = Item("Axe", "123")
        self.core.current_location = Location("Lake", "123", ["Home"], [unit], [item])
        self.core.attack(unit)
        self.assertTrue("Axe" in self.core.current_location.items)



