from abstract_handler import AbstractHandler
from move import Move

class Winner(AbstractHandler):
  def process_request(self, move: Move) -> Move:
    if(move.valid):
      possibilities = []

      possibilities.append(move.board[0:3])
      possibilities.append(move.board[3:6])
      possibilities.append(move.board[6:])

      possibilities.append(move.board[0::3])
      possibilities.append(move.board[1::3])
      possibilities.append(move.board[2::3])

      possibilities.append(move.board[0::4])
      possibilities.append(move.board[2:7:2])

      if(['X'] * 3 in possibilities):
        move.winner = 'X'
      elif(['O'] * 3 in possibilities):
        move.winner = 'O'
      else:
        move.winner = False

    return move