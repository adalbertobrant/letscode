
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

  
# área principal do programa

if __name__ == "__main__":
  window = Window()
  window.mainloop()

