from tkinter import *
import setting
import utils
from cell import Cell

root = Tk()
##overide the settings of the window
root.configure(bg = 'black')
root.geometry(f'{setting.WIDTH}x{setting.HEIGHT}')
root.title('Minesweeper game')
root.resizable(False,False)

top_frame = Frame(root, bg='black', width=setting.WIDTH, height=utils.height_prct(25))
top_frame.place(x=0, y=0)

left_frame = Frame(root, bg='black', width=360, height=540)
left_frame.place(x=0, y=utils.height_prct(25))

center_frame = Frame(root, bg='black',width=utils.width_prct(75),height=utils.height_prct(75))
center_frame.place(x=utils.width_prct(25),y=utils.height_prct(25))

for x in range(setting.GRID_SIZE):
    for y in range(setting.GRID_SIZE):
        c=Cell(x,y)
        c.create_btn_object(location=center_frame)
        c.cell_btn_object.grid(column=x, row=y)

Cell.create_cell_count_label(left_frame)
Cell.cell_count_label_object.place(x=0, y=0)

Cell.randomize_mines()

#run the window
root.mainloop()