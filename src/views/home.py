from tkinter import Frame, Label, Button, Entry, W, E, BOTH, YES

class HomeView(Frame):
  def __init__(self, main_view, root):
    Frame.__init__(self, root)

    self.NUMBER_PLAYERS = 2
    self.BASE_NAME_PLAYER = 'Jogador'
    self.BASE_NAME_PLAYER_SYMBOLS = ['X', 'O', '$', '@']

    self.root = root
    self.main_view = main_view

    self.define_header()
    self.define_form()
    self.define_ranking()

  def define_header(self):
    self.header = {
      'container': None,
      'title': None
    }

    self.header['container'] = Frame(self)
    self.header['container'].grid()
    self.header['title'] = Label(self.header['container'], text='Jogo da Velha')
    self.header['title'].grid(row=1, column=0, columnspan=2, sticky=W+E)

  def define_form(self):
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
  
  def define_ranking(self):
    self.ranking = {
      'container': None,
      'title': None,
      'columns': {
        'position': None,
        'nickname': None,
        'wins': None
      }
    }

    self.ranking['container'] = Frame(self)
    self.ranking['container'].grid()
    self.ranking['title'] = Label(self.ranking['container'], text='Ranking')
    self.ranking['title'].grid(row=self.NUMBER_PLAYERS + 2, column=0, columnspan=3, sticky=W+E)

    self.ranking['columns']['position'] = Label(self.ranking['container'], text='Posição')
    self.ranking['columns']['position'] .grid(row=self.NUMBER_PLAYERS + 3, column=0, sticky=W+E)
    
    self.ranking['columns']['nickname'] = Label(self.ranking['container'], text='Nickname')
    self.ranking['columns']['nickname'] .grid(row=self.NUMBER_PLAYERS + 3, column=1, sticky=W+E)

    self.ranking['columns']['wins']  = Label(self.ranking['container'], text='Vitórias')
    self.ranking['columns']['wins'] .grid(row=self.NUMBER_PLAYERS + 3, column=2, sticky=W+E)

    self.ranking['items'] = Frame(self.ranking['container'])
    self.ranking['items'].grid(row=self.NUMBER_PLAYERS + 4, column=0, columnspan=3, sticky=W+E)

    players_ranking = self.main_view.get_ranking()

    self.set_ranking(players_ranking)

  def reset_ranking(self):
    if not self.ranking['items'] == None:
      for widget in self.ranking['items'].winfo_children():
        widget.destroy()

  def set_ranking(self, ranking):
    self.reset_ranking()    

    base_row = self.NUMBER_PLAYERS + 4
    count = 1

    for player in ranking:
      current_row = base_row + count
      
      Label(self.ranking['items'], text=f'# {count}').grid(row=current_row, column=0, sticky=W+E)
      Label(self.ranking['items'], text=player['nickname']).grid(row=current_row, column=1, sticky=W+E)
      Label(self.ranking['items'], text=player['wins']).grid(row=current_row, column=2, sticky=W)
      
      count += 1

  def get_players(self):
    players = {}

    for count in range(self.NUMBER_PLAYERS):
      player_dict_key = f'player_{count + 1}'

      players[player_dict_key] = self.form['players'][player_dict_key]['entry'].get()

      if(not players[player_dict_key]):
        players[player_dict_key] = f'{self.BASE_NAME_PLAYER} {self.BASE_NAME_PLAYER_SYMBOLS[count]}'
    
    return players