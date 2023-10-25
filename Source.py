import tkinter as tk
import numpy as np
from class_list import *


root = tk.Tk()
canvas = tk.Canvas(root, width = canvas_width, height = canvas_height)
canvas.pack()

platform = Platform(50, canvas)
pongball = Ball(canvas)

def animate():
    pongball.move()
    check(platform,pongball)
    root.after(20, animate)

animate()
root.mainloop()

