
from player import Player

class TennisGame:
    def __init__(self, player1_name, player2_name):
        self._players = {
            player1_name: Player(player1_name),
            player2_name: Player(player2_name)
        }

    def won_point(self, player_name):
        self._players[player_name].won_point()

    def _even_score(self, given_score:int):
        if given_score == 0:
            return "Love-All"
        elif given_score == 1:
            return "Fifteen-All"
        elif given_score == 2:
            return "Thirty-All"
        else:
            return "Deuce"

    def _winning(self, p1_score:int, p2_score:int):
        minus_result = p1_score - p2_score

        if minus_result == 1:
            return "Advantage player1"
        elif minus_result == -1:
            return "Advantage player2"
        elif minus_result >= 2:
            return "Win for player1"
        else:
            return "Win for player2"

    def _ongoing(self, p1_score:int, p2_score:int):
        score = ""
        temp_score = 0
        for i in range(1, 3):
            if i == 1:
                temp_score = p1_score
            else:
                score = score + "-"
                temp_score = p2_score

            if temp_score == 0:
                score = score + "Love"
            elif temp_score == 1:
                score = score + "Fifteen"
            elif temp_score == 2:
                score = score + "Thirty"
            elif temp_score == 3:
                score = score + "Forty"
        return score

    def get_score(self):
        _player_names = list(self._players.keys())
        score = ""

        p1_score,p2_score = self._players[_player_names[0]].get_score(),self._players[_player_names[1]].get_score()

        if p1_score == p2_score:
            score = self._even_score(p1_score)
        elif p1_score >= 4 or p2_score >= 4:
            score = self._winning(p1_score, p2_score)
        else:
            score = self._ongoing(p1_score, p2_score)

        return score
