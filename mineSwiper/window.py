from tkinter import *
import tkinter as tk
import settings as ss
import utils 
from cell import Cell

class Window(tk.Tk):

  def __init__(self):
    super().__init__()
    self.configure(bg='black')
    self.geometry(f"{ss.WIDTH}x{ss.HEIGHT}")
    self.resizable(False,False)
    self.title("Mine Sweeper")
    # Frame creation 
    top_frame = Frame(
      self,
      bg='green',
      width=ss.WIDTH,
      height=utils.height_prct(25)
    )
    top_frame.place(x=0, y=0)

    game_title = Label(
      top_frame, 
      bg='black',
      fg='white',
      text='MineSweeper Game, by Adalberto Filho',
      font=('', 30),
    )

    game_title.place(
      x=utils.width_prct(25),
      y=utils.height_prct(7),
    )

    left_frame = Frame(
      self,
      bg='black',
      width=utils.width_prct(25),
      height=utils.height_prct(75)
    )

    left_frame.place(x=0, y=utils.height_prct(25))

    center_frame = Frame(
      self,
      bg='yellow',
      width=utils.width_prct(75),
      height=utils.height_prct(75)
    )

    center_frame.place(
      x=utils.width_prct(25),
      y=utils.height_prct(25)
    )

    for x in range(ss.GRID_SIZE):
      for y in range(ss.GRID_SIZE):
        c1 = Cell(x,y)
        c1.create_btn_object(center_frame)
        c1.cell_btn_object.grid(
          column=x,
          row=y
        )

# calling the label from cell class 
    Cell.create_cell_count_label(left_frame)
    Cell.cell_count_label_object.place(
      x=0,y=0
      )

    Cell.randomize_mines()



    
# área principal do programa

if __name__ == "__main__":
  window = Window()
  window.mainloop()

