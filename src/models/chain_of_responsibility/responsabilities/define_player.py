from abstract_handler import AbstractHandler
from move import Move

class DefinePlayer(AbstractHandler):
  def process_request(self, move: Move) -> Move:
    blank_positions = move.board.count(' ')

    if(blank_positions % 2):
      move.player = 'X'
    else:
      move.player = 'O'

    return move
