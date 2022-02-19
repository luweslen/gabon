from tkinter import Frame, Label, Button, W, E

class GameView(Frame):
  def __init__(self, main_view, root):
    Frame.__init__(self, root)

    self.root = root
    self.main_view = main_view

    self.draw_header()
    self.draw_board()
    self.draw_footer()

  def draw_header(self):
    self.header = {
      'container': None,
      'title': None
    }
    
    self.header['container'] = Frame(self)
    self.header['container'].grid()
    self.header['title'] = Label(self.header['container'], text='O jogo começou!')
    self.header['title'].grid(row=1, column=0, columnspan=2, sticky=W+E)
  
  def draw_board(self):
    self.board = {
      'container': None,
    }

    self.board['container'] = Frame(self)
    self.board['container'].grid()

    for button_number in range(9):
      button_name = 'button' + str(button_number)

      self.board[button_name] = Button(
      self.board['container'],
        width=10,
        height=5,
      )
      self.board[button_name].grid(row=int(button_number / 3), column=button_number % 3)

  def draw_footer(self):
    self.footer = {
      'container': None,
      'button': None,
    }

    self.footer['container'] = Frame(self)
    self.footer['container'].grid()
    self.footer['button'] = Button(
    self.footer['container'],
      width=20,
      text="Empatar",
      command=self.no_winner
    )
    self.footer['button'].grid(row=3, column=1)

  def no_winner(self):
    self.main_view.show_messagebox(title="Empatou o jogo!", message="O jogo ficou empatado e não teve um ganhador!")
    self.main_view.open_view('home')