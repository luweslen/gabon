from models.game.match import Match

class GameController:
  def __init__(self, view):
    self.view = view
    self.clean_board = [''] * 9
  
  def start_game(self, players):
    self.match = Match(players)
    self.view.draw_board(self.clean_board)

  def click_position(self, position):
    valid, winner, no_winner, board = self.match.executeMove(position)

    self.view.draw_board(board)

    if(winner):
      self.view.winner(winner)

    if(no_winner):
      self.view.no_winner()

    if(winner or no_winner):
      self.view.open_view()