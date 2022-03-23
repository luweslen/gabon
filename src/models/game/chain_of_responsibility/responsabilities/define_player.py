from models.game.chain_of_responsibility.responsabilities.abstract_handler import AbstractHandler
from models.game.move import Move

class DefinePlayer(AbstractHandler):
  def process_request(self, move: Move) -> Move:
    blank_positions = move.board.count('')

    if(blank_positions % 2 == 0):
      move.player = 'O'
    else:
      move.player = 'X'
      
    return move
