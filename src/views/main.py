from tkinter import Tk, messagebox, PhotoImage

from .home import HomeView
from .game import GameView

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

    self.views['home'] = HomeView(self, self.root)
    self.views['home'].grid(row=0, column=0, sticky='nsew')

    self.views['game'] = GameView(self, self.root)
    self.views['game'].grid(row=0, column=0, sticky='nsew')
    
    self.open_view()
    
    self.root.mainloop()

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