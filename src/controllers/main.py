class MainController:
  def __init__(self, view):
    self.view = view
  
  def start_game(self, players):
    print('Nome do jogador 1: ' + players['player_1'])
    print('Nome do jogador 2: ' + players['player_2'])