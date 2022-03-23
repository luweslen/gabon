from tkinter import Frame, Label, Button, W, E
from functools import partial

class GameView(Frame):
  def __init__(self, main_view, container):
    Frame.__init__(self, container)

    self.main_view = main_view

    self.define_header()
    self.define_board()
    self.define_footer()

  def define_header(self):
    self.header = {
      'container': None,
      'title': None
    }
    
    self.header['container'] = Frame(self)
    self.header['container'].grid()
    self.header['title'] = Label(self.header['container'], text='O jogo começou!')
    self.header['title'].grid(row=1, column=0, columnspan=2, sticky=W+E)
  
  def define_board(self):
    self.board = {
      'container': None,
      'buttons': {}
    }

    self.board['container'] = Frame(self)
    self.board['container'].grid()

    for button_number in range(9):
      button_name = 'button' + str(button_number)
      
      row = int(button_number / 3)
      column = button_number % 3

      self.board['buttons'][button_name] = Button(
        self.board['container'],
        width=10,
        height=5,
        command=partial(self.click_position, button_number)
      )
      self.board['buttons'][button_name].grid(row=row, column=column)

  def define_footer(self):
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
      command=self.main_view.no_winner
    )
    self.footer['button'].grid(row=3, column=1)

  def draw_board(self, board):
    for button_number in range(len(board)):
      button_name = 'button' + str(button_number)
      
      self.board['buttons'][button_name]['text'] = board[button_number]

  def click_position(self, position):
    self.main_view.click_position(position)