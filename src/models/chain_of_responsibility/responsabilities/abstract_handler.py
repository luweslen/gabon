import abc
from move import Move

class AbstractHandler(metclass = abc.ABCMeta):
  @abc.abstractclassmethod
  def process_request(self, move: Move) -> Move:
    raise NotImplementedError('Class not yet implemented')