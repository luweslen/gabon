from move import Move

from responsabilities.define_player import DefinePlayer
from responsabilities.validity import Validity
from responsabilities.execute_move import ExecuteMove
from responsabilities.winner import Winner
from responsabilities.no_winner import NoWinner

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