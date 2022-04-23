from tkinter import Button, Label, messagebox
import random
import settings as ss
import sys

class Cell:
  all = [ ]
  cell_count_label_object = None 
  cell_count = ss.CELL_COUNT
  def __init__(self, x, y, is_mine=False):
    self.is_mine = is_mine
    self.is_opened = False 
    self.is_mine_candidate = False
    self.cell_btn_object = None 
    self.x = x
    self.y = y
    
    # append the object to Cell.all list
    Cell.all.append(self)

  def create_btn_object(self, location):
      btn = Button(
        location,
        width = 3, 
        height = 2,
        #activeforeground ='gray85', activebackground ='gray85',
        #text = f"x{self.x},y{self.y}"
      )
      btn.bind('<Button-1>', self.left_click_actions ) #left click mouse
      btn.bind('<Button-3>', self.right_click_actions )
      self.cell_btn_object = btn

  @staticmethod # pois ele é chamado apenas uma vez e não para cada cell object
  def create_cell_count_label(location):
    lbl = Label(
      location, 
      bg='black',
      fg='white',
      font=("",30),
      text=f"Cells left: {Cell.cell_count}"

    )
    Cell.cell_count_label_object = lbl

  
  def left_click_actions(self,event):
    if self.is_mine:
      self.show_mine()
    else:
      if self.surrounded_cells_mines_length == 0:
        for cell_obj in self.surrounded_cells:
          cell_obj.show_cell()
      self.show_cell()
      # if mines equals to cells left count , player won the Game
      if Cell.cell_count == ss.MINES_COUNT:
        messagebox.showinfo(title="---Winner---", message="  You won the Game  ")
        sys.exit()


    # cancel left and right click events if cell is opened
    if self.is_opened:
      self.cell_btn_object.unbind('<Button-1>')
      self.cell_btn_object.unbind('<Button-3>')


  def get_cell_by_axis(self, x, y):
    # return a cell object based on the value of x and y
    for cell in Cell.all:
      if cell.x == x and cell.y == y:
        return cell

  @property # use as an attribute
  def surrounded_cells(self):
    cells = [
      self.get_cell_by_axis(self.x - 1, self.y - 1),
      self.get_cell_by_axis(self.x - 1, self.y),
      self.get_cell_by_axis(self.x - 1, self.y + 1),
      self.get_cell_by_axis(self.x, self.y - 1),
      self.get_cell_by_axis(self.x + 1, self.y - 1),
      self.get_cell_by_axis(self.x + 1, self.y),
      self.get_cell_by_axis(self.x + 1, self.y + 1),
      self.get_cell_by_axis(self.x, self.y + 1)
    ]
    cells = [ cell for cell in cells if cell is not None]
    return cells
  
  # count the mines in the neighborr area 
  @property
  def surrounded_cells_mines_length(self):
    counter = 0
    for cell in self.surrounded_cells:
      if cell.is_mine:
        counter += 1
    return counter


  def show_cell(self):
    if not self.is_opened:
      Cell.cell_count -= 1
      self.cell_btn_object.configure(
        text=self.surrounded_cells_mines_length,
        )
    # replace the text of cell count label with the newer count 
      if Cell.cell_count_label_object:
        Cell.cell_count_label_object.configure(
          text=f"Cells Left: {Cell.cell_count}"
        )   
        # if this was a mine candidate
        # configure the button to gray85
      self.cell_btn_object.configure(
        bg='gray85', activebackground ='gray85', 
      ) 
    # mark the cell is opened 
    self.is_opened = True 


  
  def show_mine(self):
    # message box and option to restart or close the game
    #question = messagebox.askretrycancel(title='Game Over', message="Game Over!!")
    #if question:
     # messagebox.askquestion(title='New Game', message='Press yes for new game')
    loose_game = messagebox.showerror(title='Game Over', message='Sorry, You Loose the Game!')
    new_game = messagebox.askquestion(title= "New Game", message="Press Yes for new Game")
    if new_game == 'yes':
      print("criar novo jogo")
      
    else:
      print(loose_game)
      sys.exit()

    # a logic to stop de game and display a message that player lost
    self.cell_btn_object.configure(
      bg = 'red',
      #highlightbackground='red',
      #fg='red',
      activebackground = 'red',

    )

  def right_click_actions(self, event):
    if not self.is_mine_candidate:
      self.cell_btn_object.configure(
        bg='black',
        activebackground='black',
      )
      self.is_mine_candidate = True
    else:
      self.cell_btn_object.configure(
        bg="gray85"
      )
      self.is_mine_candidate = False

  @staticmethod
  def randomize_mines():
    picked_cells = random.sample(
      Cell.all,
      ss.MINES_COUNT
    )
    for x in picked_cells:
      x.is_mine = True

  def __repr__(self):
    return f"Cell({self.x}, {self.y})"