from tkinter import Tk, Frame, messagebox, PhotoImage

from .home import HomeView
from .game import GameView

from controllers.game import GameController
from controllers.ranking import RankingController

class MainView():
  def __init__(self):
    self.root = Tk()
    self.root.geometry('700x750')

    self.root.title('GabonPY')

    self.root.iconphoto(False, PhotoImage(file = './src/assets/icon.png'))

    self.views = {
      'home': None,
      'game': None
    }

    self.main_container = Frame(self.root)
    self.main_container.pack()

    self.controllers = {
      'game': GameController(self),
      'ranking': RankingController(self),
    }

    self.views['home'] = HomeView(self, self.main_container)
    self.views['home'].grid(row=0, column=0, sticky='nsew')

    self.views['game'] = GameView(self, self.main_container)
    self.views['game'].grid(row=0, column=0, sticky='nsew')
    
    self.open_view()
    
    self.root.mainloop()

  def start_game(self):
    players = self.views['home'].get_players()

    response_valid_players = self.controllers['ranking'].check_players(players)

    if(type(response_valid_players) is dict and 'error' in response_valid_players):
      self.show_messagebox(response_valid_players['error'])
    else:
      self.controllers['game'].start_game(players)

      self.open_view('game')

  def no_winner(self):
    self.show_messagebox(title="Ocorreu um empate", message="O jogo ficou empatado e não teve um ganhador!")
    self.open_view('home')

  def winner(self, winner):
    self.controllers['ranking'].update_player(winner)
    self.show_messagebox(f'O ganhador foi o jogador {winner}')

  def open_view(self, name_view='home'):
    self.views[name_view].tkraise()
  
  def draw_board(self, board):
    self.views['game'].draw_board(board)

  def click_position(self, position):
    self.controllers['game'].click_position(position)

  def get_ranking(self):
    ranking = self.controllers['ranking'].get_players()

    return ranking

  def show_messagebox(self, message, type='showinfo', title=None):
    if type == 'showinfo':
      result = messagebox.showinfo(title=title, message=message)
    elif type == 'showerror':
      result = messagebox.showerror(title=title, message=message)
    elif type == 'askquestion':
      result = messagebox.askquestion(title=title, message=message)

    return result