
class Move():
  def __init__(self, options_move):
    self.board = options_move['board'] if 'board' in options_move else None
    self.position = options_move['position'] if 'position' in options_move else None
    self.player = options_move['player'] if 'player' in options_move else None
    self.winner = options_move['winner'] if 'winner' in options_move else None
    self.no_winner = options_move['no_winner'] if 'no_winner' in options_move else None
    self.valid = False
