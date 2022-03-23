from models.game.chain_of_responsibility.main import ChainOfResponsibility

class Match(ChainOfResponsibility):
  def __init__(self, players):
    ChainOfResponsibility.__init__(self)

    self.player_1 = players['player_1']
    self.player_2 = players['player_2']

    self.board = [''] * 9

  def executeMove(self, position):
    move = self.run(self.board, position)
    winner = ''
    valid = move.valid
    no_winner = move.no_winner
    board = move.board

    if(move.valid):
      self.board = move.board

    if(move.winner == 'X'):
      winner = self.player_1
    elif(move.winner == 'O'):
      winner = self.player_2

    return valid, winner, no_winner, board