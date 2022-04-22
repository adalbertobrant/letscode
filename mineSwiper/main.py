from tkinter import *
import settings as ss
import utils 
from cell import Cell

# create an window
root = Tk()
# configure de color
root.configure(bg='black')
# size of the window
root.geometry(f"{ss.WIDTH}x{ss.HEIGHT}")
# make the window not resizable
root.resizable(False, False)
# change the title of the window
root.title("MineSweeper")

# Frame creation 
top_frame = Frame(
  root,
  bg='black',
  width=ss.WIDTH,
  height=utils.height_prct(25)
)

top_frame.place(x=0, y=0)

left_frame = Frame(
  root,
  bg='black',
  width=utils.width_prct(25),
  height=utils.height_prct(75)
)

left_frame.place(x=0, y=utils.height_prct(25))

center_frame = Frame(
  root,
  bg='black',
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

Cell.randomize_mines()



# loop the window until the user close
root.mainloop()

