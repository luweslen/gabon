from abstract_handler import AbstractHandler
from move import Move

class NoWinner(AbstractHandler):
  def process_request(self, move: Move) -> Move:
    if(move.valid and not move.winner):

      if(move.board.count('') == 0):
        move.no_winner = True
      else:
        move.no_winner = False

    return move