
class Player:
    def __init__(self, name:str):
        self._name = name
        self._score = 0

    def won_point(self):
        self._score += 1

    def get_score(self):
        return self._score

    def get_name(self):
        return self._name