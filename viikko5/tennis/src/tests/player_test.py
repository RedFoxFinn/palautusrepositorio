
import unittest

from player import Player

class TestPlayer(unittest.TestCase):
    def setUp(self):
        self.player = Player("player1")

    def test_constructor(self):
        self.assertEqual(self.player.get_name(), "player1")
        self.assertEqual(self.player.get_score(), 0)

    def test_won_point(self):
        self.player.won_point()
        self.assertEqual(self.player.get_score(), 1)
        self.player.won_point()
        self.assertEqual(self.player.get_score(), 2)