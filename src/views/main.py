from tkinter import Tk, Frame, messagebox, PhotoImage

from .home import HomeView
from .game import GameView

from controllers.main import MainController

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

    self.views['home'] = HomeView(self, self.main_container)
    self.views['home'].grid(row=0, column=0, sticky='nsew')

    self.views['game'] = GameView(self, self.main_container)
    self.views['game'].grid(row=0, column=0, sticky='nsew')

    self.controller = MainController(self)
    
    self.open_view()
    
    self.root.mainloop()

  def start_game(self):
    players = self.views['home'].get_players()

    self.controller.start_game(players)

    self.open_view('game')

  def no_winner(self):
    self.show_messagebox(title="Ocorreu um empate", message="O jogo ficou empatado e não teve um ganhador!")
    self.open_view('home')

  def open_view(self, name_view='home'):
    self.views[name_view].tkraise()
  
  def show_messagebox(self, message, type='showinfo', title=None):
    if type == 'showinfo':
      result = messagebox.showinfo(title=title, message=message)
    elif type == 'showerror':
      result = messagebox.showerror(title=title, message=message)
    elif type == 'askquestion':
      result = messagebox.askquestion(title=title, message=message)

    return result