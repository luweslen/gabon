from models.ranking import Ranking

class RankingController:
  def __init__(self, view):
    self.view = view
    self.ranking = Ranking()
  
  def check_players(self, players):
    new_dict = {}
    for key, value in players.items():
      new_dict.setdefault(value, set()).add(key)

    has_duplicate_nickname = [key for key, values in new_dict.items() if len(values) > 1]

    if(has_duplicate_nickname):
      return {
        'error': 'Nomes duplicados'
      }

    for key in players:
      nickname = players[key]
      player = self.ranking.get_player(nickname)

      if(not player):
        body = {
          'nickname': nickname,
          'wins': 0
        }
        self.ranking.add_player(body)
    
  def update_player(self, nickname):
    player = self.ranking.get_player(nickname)
    updated = self.ranking.update_wins(player['_id'])

  def get_players(self):
    players = self.ranking.get_players()
    return players