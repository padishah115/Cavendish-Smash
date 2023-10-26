import tkinter as tk
import numpy as np
from constants import *
from platform_class import *
from ball import *
from block import *

root = tk.Tk()
MyCanvas = tk.Canvas(root, width = canvas_width, height = canvas_height)
MyCanvas.pack()

platform = Platform(100, MyCanvas)
pongball = Ball(MyCanvas)

create_grid(10, 10, 20, 10, MyCanvas)

def animate():
    pongball.move()
    pongball.check(platform)
    root.after(20, animate)

animate()
root.mainloop()

