import tkinter as tk
import numpy as np
from constants import *
from platform_class import *
from ball import *
from block import *


root = tk.Tk()
MyCanvas = tk.Canvas(root, width = canvas_width, height = canvas_height)
MyCanvas.pack()

platform = Platform(50, MyCanvas)
pongball = Ball(MyCanvas)

create_grid(2, 2, 10, 10, MyCanvas)

def animate():
    pongball.move()
    check(platform,pongball)
    root.after(20, animate)

animate()
root.mainloop()

