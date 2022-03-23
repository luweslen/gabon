from models.game.chain_of_responsibility.responsabilities.abstract_handler import AbstractHandler
from models.game.move import Move

class ExecuteMove(AbstractHandler):
  def process_request(self, move: Move) -> Move:
    if(move.valid):
      move.board[move.position] = move.player

    return move