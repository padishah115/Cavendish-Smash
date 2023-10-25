#block
import tkinter as tk
import numpy as np
from constants import *
from platform_class import *
from ball import *

class Block:
    """Block Class"""
    def __init__(self, position, width, height, color, canvas):
        self.position = position
        self.width = width
        self.height = height
        self.color = color
        self.canvas = canvas

        self.rectangle = 0
    
    def draw(self):
        x1 = self.position[0] - self.width / 2
        x2 = self.position[0] + self.width / 2
        y1 = self.position[1] + self.height / 2
        y2 = self.position[1] - self.height / 2

        self.rectangle = self.canvas.create_rectangle(x1, y1, x2, y2, fill = self.color)



def create_grid(rows, columns, width, height, canvas):
    com = np.array([canvas_height/4, canvas_width/2])

    for i in range(0, rows):
        x = -rows / 2
        for j in range (0, columns):
            y = -columns / 2
            new_block = Block(com + np.array([y*width/2, x*width/2]), width, height, "red", canvas)
            new_block.draw()
            y += 1
        x += 1