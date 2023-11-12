class Player:
    def __init__(self, dict):
        self.name = dict['name']
        self.nationality = dict['nationality']
        self.assists = dict['assists']
        self.goals = dict['goals']
        self.penalties = dict['penalties']
        self.team = dict['team']
        self.games = dict['games']

    def get_name(self):
        return self.name
    def get_nationality(self):
        return self.nationality
    def get_assists(self):
        return self.assists
    def get_goals(self):
        return self.goals
    def get_penalties(self):
        return self.penalties
    def get_team(self):
        return self.team
    def get_games(self):
        return self.games
    def get_points(self):
        return self.goals + self.assists

    def __str__(self):
        return f"{self.get_name():24}   {self.get_team()}   {self.get_goals()} + {self.get_assists()} = {self.get_points()}"
