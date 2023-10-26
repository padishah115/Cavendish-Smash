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

        bodies.append(self)

        self.rectangle = self.canvas.create_rectangle(x1, y1, x2, y2, fill = self.color)

    def delete(self):
        self.canvas.delete(self.rectangle)
        bodies.remove(self)


def create_grid(rows, columns, width, height, canvas):
    center_of_mass = np.array([canvas_width/2, canvas_height/4])
    x_i = center_of_mass[0] - (columns * width) / 2
    y_i = center_of_mass[1] - (rows * height) /2

    for i in range(0, rows):
        for j in range (0, columns):
            x_new = x_i + j*width
            y_new = y_i + i*height

            new_position = np.array([x_new, y_new])
            new_block = Block(new_position, width, height, "red", canvas)
            new_block.draw()