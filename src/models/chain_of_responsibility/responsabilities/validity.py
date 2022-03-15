from abstract_handler import AbstractHandler
from move import Move

class Validity(AbstractHandler):
  def process_request(self, move: Move) -> Move:
    if(move.board[move.position] == ''):
      move.valid = True

    return move