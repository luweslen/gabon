from tkinter import Frame, Label, Button, Entry, W, E, BOTH, YES

class HomeView(Frame):
  def __init__(self, main_view, root):
    Frame.__init__(self, root)

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
      'player1': {
        'label': None,
        'value': None,
      },
      'player2': {
        'label': None,
        'value': None,
      },
      'button': None
    }

    self.form['container'] = Frame(self)
    self.form['container'].grid()
    self.form['player1']['label'] = Label(self.form['container'], text='Jogador 1: ')
    self.form['player1']['label'] .grid(row=1, column=0, sticky=W+E)
    self.form['player1']['value'] = Entry(self.form['container'])
    self.form['player1']['value'].grid(row=1, column=1, sticky=W+E)

    self.form['player2']['label'] = Label(self.form['container'], text='Jogador 2: ')
    self.form['player2']['label'] .grid(row=2, column=0, sticky=W+E)
    self.form['player2']['value'] = Entry(self.form['container'])
    self.form['player2']['value'].grid(row=2, column=1, sticky=W+E)
    
    self.form['button'] = Button(
      self.form['container'],
      width=20,
      text="Jogar",
      command=self.valid_form
    )
    self.form['button'].grid(row=3, column=1)
    
  def valid_form(self):
    player1 = self.form['player1']['value'].get()
    player2 = self.form['player1']['value'].get()

    if((not player1) or (not player2)):
      self.main_view.show_messagebox(message="Preencha os nomes dos jogadores", title="Encontramos um erro")
    else:
      self.main_view.open_view('game')