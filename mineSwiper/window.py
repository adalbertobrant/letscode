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

    
# área principal do programa

if __name__ == "__main__":
  window = Window()
  window.mainloop()

