import abc

from models.game.move import Move

class AbstractHandler(metaclass = abc.ABCMeta):
  @abc.abstractclassmethod
  def process_request(self, move: Move) -> Move:
    raise NotImplementedError('Class not yet implemented')