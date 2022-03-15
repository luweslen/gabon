from abstract_handler import AbstractHandler
from move import Move

class ExecuteMove(AbstractHandler):
  def process_request(self, move: Move) -> Move:
    if(move.valid):
      move.board[move.position] = move.player

    return move