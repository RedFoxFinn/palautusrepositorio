
class PlayerStats:
    def __init__(self, reader):
        self._player_reader = reader

    def top_scorers_by_nationality(self, nationality:str):
        players = self._player_reader.get_players()
        returnable = []
        for player in players:
            if player.get_nationality() == nationality:
                returnable.append(player)
        print(f"Players from {nationality}\n")
        return returnable