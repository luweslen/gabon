from tkinter import Frame, Label, Button, Entry, ttk, W, E, BOTH, YES, NO, CENTER

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
      'table': None
    }

    self.ranking['container'] = Frame(self)
    self.ranking['container'].grid(row=self.NUMBER_PLAYERS + 2, column=0, columnspan=3, sticky=W+E)
    self.ranking['title'] = Label(self.ranking['container'], text='Ranking')
    self.ranking['title'].grid(row=self.NUMBER_PLAYERS + 2, column=0, columnspan=3, sticky=W+E)

    style = ttk.Style()
    style.configure('Treeview', rowheight=50)

    self.ranking['table'] = ttk.Treeview(self.ranking['container'])

    self.ranking['table']['columns'] = ('position', 'nickname', 'wins')

    self.ranking['table'].column("#0", width=0, stretch=NO)
    self.ranking['table'].column("position", anchor=CENTER, width=160)
    self.ranking['table'].column("nickname", anchor=CENTER, width=160)
    self.ranking['table'].column("wins", anchor=CENTER, width=160)

    self.ranking['table'].heading("#0",text="", anchor=CENTER)
    self.ranking['table'].heading("position", text="Posição", anchor=CENTER)
    self.ranking['table'].heading("nickname", text="Nickname", anchor=CENTER)
    self.ranking['table'].heading("wins", text="Vitórias", anchor=CENTER)
    
    self.ranking['table'].grid(row=self.NUMBER_PLAYERS + 3, column=0, columnspan=3, sticky=W+E)

    players_ranking = self.main_view.get_ranking()

    self.set_ranking(players_ranking)

  def reset_ranking(self):
    for i in self.ranking['table'].get_children():
      self.ranking['table'].delete(i)

  def set_ranking(self, ranking):
    self.reset_ranking()    

    base_row = self.NUMBER_PLAYERS + 4
    count = 1

    for player in ranking:
      current_row = base_row + count
      
      self.ranking['table'].insert(
        parent='',
        index='end',
        iid=count - 1,
        text='',
        values=(f'#{count}', player['nickname'], player['wins'])
      )
      
      count += 1

  def get_players(self):
    players = {}

    for count in range(self.NUMBER_PLAYERS):
      player_dict_key = f'player_{count + 1}'

      players[player_dict_key] = self.form['players'][player_dict_key]['entry'].get()

      if(not players[player_dict_key]):
        players[player_dict_key] = f'{self.BASE_NAME_PLAYER} {self.BASE_NAME_PLAYER_SYMBOLS[count]}'
    
    return players