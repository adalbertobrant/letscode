from tkinter import Button
import random
import settings as ss

class Cell:
  all = [ ]
  def __init__(self, x, y, is_mine=False):
    self.is_mine = is_mine
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
        #text = f"x{self.x},y{self.y}"

      )
      btn.bind('<Button-1>', self.left_click_actions ) #left click mouse
      btn.bind('<Button-3>', self.right_click_actions )
      self.cell_btn_object = btn

  def left_click_actions(self,event):
    if self.is_mine:
      self.show_mine()
    else:
      self.show_cell()

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
    self.cell_btn_object.configure(text=self.surrounded_cells_mines_length)

  
  def show_mine(self):
    # a logic to stop de game and display a message that player lost
    self.cell_btn_object.configure(
      bg = 'red'
    )

  def right_click_actions(self, event):
    print(event)
    print(" ")
    print("I am right clicked!")
    print("------")

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