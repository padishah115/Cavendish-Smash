import tkinter as tk
import numpy as np
from constants import *
from ball import *
from block import Block

class Platform:
    """Platform Class: This encodes the properties of the moveable rectangle in Python"""
    def __init__(self, width, canvas, movement_speed = 10):
        self.x1, self.y1, self.x2, self.y2 = 400-width/2, 700, 400+width/2, 710
        self.canvas = canvas
        self.rectangle = canvas.create_rectangle(self.x1, self.y1, self.x2, self.y2, fill = "blue") #Arguments: x1, y1, x2, y2
        self.canvas.bind_all("<KeyPress-Left>", self.move_left)
        self.canvas.bind_all("<KeyPress-Right>", self.move_right)

        self.movement_speed = movement_speed

        x_com = self.x1 + 0.5 * (self.x2 - self.x1)
        y_com = self.y1 + 0.5 * (self.y2 - self.y1)

        self.position = np.array([x_com, y_com])

    def move_left(self, event):
        """Moves the platform left when the player uses the left arrow key"""
        self.canvas.move(self.rectangle, -1*self.movement_speed, 0)
        self.position[0] -= self.movement_speed
        self.x1 -= self.movement_speed
        self.x2 -= self.movement_speed

    def move_right(self, event):
        """Moves the platform right when the player presses the right arrow key"""
        self.canvas.move(self.rectangle, self.movement_speed, 0)
        self.position[0] += self.movement_speed
        self.x1 += self.movement_speed
        self.x2 += self.movement_speed


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




