from configs.database import database

class Ranking:
  def __init__(self):
    self.database = database

  def add_player(self, body):
    created_player = self.database.ranking.insert_one(body)

    if not created_player.inserted_id:
      raise 'Erro ao criar um novo jogador, tente novamente.'

  def update_wins(self, id):
    updated_player = self.database.ranking.update_one(
      { '_id': id },
      { '$inc': { 'wins': 1 } }
    )

    if updated_player.modified_count < 1:
      raise 'Erro ao atualizar o status do jogador, tente novamente.'

  def get_player(self, nickname):
    player = self.database.ranking.find_one({ 'nickname': nickname })

    return player

  def get_players(self):
    players = self.database.ranking.find({ 'nickname': { '$nin': ['Jogador O', 'Jogador X'] } }).sort('wins', -1)

    return list(players)