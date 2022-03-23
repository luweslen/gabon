from models.game.move import Move

from models.game.chain_of_responsibility.responsabilities.define_player import DefinePlayer
from models.game.chain_of_responsibility.responsabilities.validity import Validity
from models.game.chain_of_responsibility.responsabilities.execute_move import ExecuteMove
from models.game.chain_of_responsibility.responsabilities.winner import Winner
from models.game.chain_of_responsibility.responsabilities.no_winner import NoWinner

class ChainOfResponsibility():
  def __init__(self):
    self.responsibilities = []

    self.responsibilities.append(DefinePlayer())
    self.responsibilities.append(Validity())
    self.responsibilities.append(ExecuteMove())
    self.responsibilities.append(Winner())
    self.responsibilities.append(NoWinner())

  def run(self, board, position):
    move = Move({ 'board': board, 'position': position })

    for responsibility in self.responsibilities:
      move = responsibility.process_request(move)

    return move