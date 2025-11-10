from requests import get


class Player:
    def __init__(self, dict):
        self.name           = dict['name']
        self.nationality    = dict['nationality']
        self.assists        = dict['assists']
        self.goals          = dict['goals']
        self.team           = dict['team']
        self.games          = dict['games']
        self.id             = dict['id']
        
    def __str__(self):
        return self.name


class PlayerReader:
    def __init__(self, url):
        self.url = url

    def get_players(self):
        return [Player(player_dict) for player_dict in get(self.url).json()]


class PlayerStats:
    def __init__(self, reader):
        self.players = reader.get_players()

    def top_scores_by_nationality(self, nationality):
        chosen_players = []
        for player in self.players:
            if player.nationality == nationality:
                chosen_players.append(player)
        return sorted(chosen_players,
                      key=lambda p: p.assists+p.goals,
                      reverse=True)


