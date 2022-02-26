from tkinter import Frame, Label, Button, Entry, W, E, BOTH, YES

class HomeView(Frame):
  def __init__(self, main_view, root):
    Frame.__init__(self, root)

    self.NUMBER_PLAYERS = 2
    self.BASE_NAME_PLAYER = 'Jogador'
    self.BASE_NAME_PLAYER_SYMBOLS = ['X', 'O', '$', '@']

    self.root = root
    self.main_view = main_view

    self.draw_header()
    self.draw_form()

  def draw_header(self):
    self.header = {
      'container': None,
      'title': None
    }

    self.header['container'] = Frame(self)
    self.header['container'].grid()
    self.header['title'] = Label(self.header['container'], text='Jogo da Velha')
    self.header['title'].grid(row=1, column=0, columnspan=2, sticky=W+E)

  def draw_form(self):
    self.form = {
      'container': None,
      'players': {},
      'button': None
    }

    self.form['container'] = Frame(self)
    self.form['container'].grid()

    for count in range(self.NUMBER_PLAYERS):
      player_number = count + 1
      player_dict_key = f'player_{player_number}'

      self.form['players'][player_dict_key] = { 'label': None, 'entry': None }

      self.form['players'][player_dict_key]['label'] = Label(self.form['container'], text=f'Jogador {player_number}: ')
      self.form['players'][player_dict_key]['label'].grid(row=player_number, column=0, sticky=W+E)

      self.form['players'][player_dict_key]['entry'] = Entry(self.form['container'])
      self.form['players'][player_dict_key]['entry'].grid(row=player_number, column=1, sticky=W+E)

    self.form['button'] = Button(
      self.form['container'],
      width=20,
      text="Jogar",
      command=self.main_view.start_game
    )
    self.form['button'].grid(row=self.NUMBER_PLAYERS + 1, column=1)
    
  def get_players(self):
    players = {}

    for count in range(self.NUMBER_PLAYERS):
      player_dict_key = f'player_{count + 1}'

      players[player_dict_key] = self.form['players'][player_dict_key]['entry'].get()

      if(not players[player_dict_key]):
        players[player_dict_key] = f'{self.BASE_NAME_PLAYER} {self.BASE_NAME_PLAYER_SYMBOLS[count]}'
    
    return players