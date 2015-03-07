from unittest import TestCase
from core.player import Player
from core.unit import Unit


class TestPlayer(TestCase):
    def setUp(self):
        self.unit = Unit('Wolf', 30, 2, 5, [])
        self.player = Player('Player', 100, 5, 10, [])

    def test_to_death(self):
        self.player.fight(self.unit)
        self.assertFalse(self.unit.is_alive())
        self.assertTrue(self.player.is_alive())

    def test_for_damage(self):
         start_player_health = self.player.health
         self.player.fight(self.unit)
         self.assertTrue(self.player.health < start_player_health)