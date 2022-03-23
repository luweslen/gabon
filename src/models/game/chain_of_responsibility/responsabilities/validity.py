from models.game.chain_of_responsibility.responsabilities.abstract_handler import AbstractHandler
from models.game.move import Move

class Validity(AbstractHandler):
  def process_request(self, move: Move) -> Move:
    if(move.board[move.position] == ''):
      move.valid = True

    return move