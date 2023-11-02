import unittest
from statistics_service import StatisticsService, SortBy
from player import Player

class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri",   "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89)
        ]

class TestStatisticsService(unittest.TestCase):
    def setUp(self):
        # annetaan StatisticsService-luokan oliolle "stub"-luokan olio
        self.stats = StatisticsService(PlayerReaderStub())

    def test_statistics_service_returns_None_on_nonexistent_player(self):
        self.assertEqual(self.stats.search("Koivu"), None)

    def test_statistics_service_returns_player_name_on_existing_player(self):
        player = self.stats.search("Kurri")
        self.assertEqual(player.name, "Kurri")

    def test_statistics_service_returns_list_of_players_of_a_valid_team(self):
        players = self.stats.team("EDM")
        self.assertEqual(len(players), 3)

    def test_statistics_service_returns_empty_list_of_players_of_an_invalid_team(self):
        players = self.stats.team("NYR")
        self.assertEqual(len(players), 0)

    def test_statistics_service_returns_top_scorers(self):
        players = self.stats.top(2)
        self.assertEqual(len(players), 3)
        self.assertEqual(players[0].name, "Gretzky")
        self.assertEqual(players[1].name, "Lemieux")
        self.assertEqual(players[2].name, "Yzerman")

    def test_statistics_service_default_sorting_is_by_points(self):
        players = self.stats.top(2)
        self.assertEqual(players[0].name, "Gretzky")
        self.assertEqual(players[1].name, "Lemieux")

    def test_statistics_service_sorts_by_goals(self):
        players = self.stats.top(2, SortBy.GOALS)
        self.assertEqual(players[0].name, "Lemieux")
        self.assertEqual(players[1].name, "Yzerman")

    def test_statistics_service_sorts_by_assists(self):
        players = self.stats.top(2, SortBy.ASSISTS)
        self.assertEqual(players[0].name, "Gretzky")
        self.assertEqual(players[1].name, "Yzerman")

    def test_statistics_service_sorts_by_points(self):
        players = self.stats.top(2, SortBy.POINTS)
        self.assertEqual(players[0].name, "Gretzky")
        self.assertEqual(players[1].name, "Lemieux")