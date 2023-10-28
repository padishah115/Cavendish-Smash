import tkinter as tk
import numpy as np
from constants import *
from platform_class import *
from ball import *
from block import *

class Level:
    def __init__(self, velocity, rows, columns, width, height, platform_width, canvas, root, v_x_ball, v_y_ball):
        self.velocity = velocity
        self.rows = rows
        self.columns = columns
        self.width = width
        self.height = height
        self.platform_width = platform_width
        self.root = root
        self.bodies = []
        self.ball_velocity = np.array([v_x_ball, v_y_ball])
        self.canvas = canvas


    def build_level(self):
        self.create_grid(self.rows, self.columns, self.width, self.height, self.canvas, self)
        self.platform = Platform(self.platform_width, self.canvas)
        self.ball = Ball(self.canvas, self.ball_velocity[0], self.ball_velocity[1])

    def animate(self):
        self.ball.move()
        self.platform.check(self.platform)
        self.root.after(20, self.animate)
        
    def play_level(self):
        self.animate()
        self.root.mainloop()

    # def delete_level(self):


    def create_grid(self, rows, columns, width, height, canvas):
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




def create_grid(self, rows, columns, width, height, canvas):
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