#block
import tkinter as tk
import numpy as np
from constants import *
from platform_class import *
from ball import *

class Block:
    """Block Class"""
    def __init__(self, position, width, height, color, canvas, level):
        self.position = position
        self.width = width
        self.height = height
        self.color = color
        self.canvas = canvas
        self.level = level

        self.rectangle = 0
    
    def draw(self):
        x1 = self.position[0] - self.width / 2
        x2 = self.position[0] + self.width / 2
        y1 = self.position[1] + self.height / 2
        y2 = self.position[1] - self.height / 2

        self.level.bodies.append(self)

        self.rectangle = self.canvas.create_rectangle(x1, y1, x2, y2, fill = self.color)

    def delete(self):
        self.canvas.delete(self.rectangle)
        self.level.bodies.remove(self)


