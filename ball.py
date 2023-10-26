#BALL CLASS
import tkinter as tk
import numpy as np
from constants import *
from platform_class import *
from block import *


class Ball:
    """bouncing ball class, obviously"""
    def __init__(self, canvas, color = "red", radius = 10, position = np.array([400, 400])):
        self.canvas = canvas
        self.color = color
        self.radius = radius
        self.position = position

        self.oval = 0
        self.velocity = 0

        self.set_velocity() #Initialises velocity
        self.draw() #Draws ball onto canvas

    def set_velocity(self):
        v_x = np.random.uniform(-2,2)
        v_y = -5

        self.velocity = np.array([v_x, v_y])

    def draw(self):
        x1, y1 = self.position[0] - self.radius, self.position[1] - self.radius
        x2, y2 = self.position[0] + self.radius, self.position[1] + self.radius
        self.oval = self.canvas.create_oval(x1, y1, x2, y2, fill = self.color)
    
    def move(self):
        self.position = self.velocity + self.position
        self.canvas.move(self.oval, self.velocity[0], self.velocity[1])

    def reverse_y(self):
        """Reverses Y velocity"""
        self.velocity[1] *= -1

    def reverse_x(self):
        """Reverses X Velocity"""
        self.velocity[0] *= -1


    def check(self, platform1):
        """Checks ball position and changes velocity depending on whether the ball has collided with the
        walls or platform or blocks"""
        dx = platform1.position[0] - self.position[0]
        dy = platform1.position[1] - self.position[1]
        r = np.sqrt(dx**2 + dy**2)

        if self.position[0] >= platform1.x1 - self.radius and self.position[1] == platform1.y1 \
            and self.position[0] <= platform1.x2 + self.radius:
            self.reverse_y()

        if self.position[0] >= canvas_width - self.radius:
            #If ball all the way to the right hand side
            self.reverse_x()

        if self.position[0] <= self.radius:
            #If ball all the way to the left
            self.reverse_x()

        if self.position[1] <= self.radius:
            #If ball is all the way at the top
            self.reverse_y()

        if canvas_height - self.position[1] <= r:
            #THIS SHOULD LOSE YOU THE GAME!
            print("Game Over!")

        for block in bodies:
            block_x = block.position[0]
            block_y = block.position[1]
            block_width = block.width
            block_height = block.height

            block_left = block_x - block_width/2
            block_right = block_x + block_width/2
            block_top = block_y + block_height/2
            block_bottom = block_y - block_height/2

        
            #Collides with left hand side
            if self.position[0] + self.radius == block_left and self.position[1] + self.radius >= block_bottom\
                and self.position[1] - self.radius <= block_top:
                self.reverse_x()
                block.delete()
                break
                    
            #Collides with right hand side
            if self.position[0] - self.radius == block_right and self.position[1] + self.radius >= block_bottom\
                and self.position[1] - self.radius <= block_top:
                self.reverse_x()
                block.delete()
                break

            #Collides with top side
            if self.position[0] - self.radius <= block_right and self.position[0] + self.radius >= block_left\
                and self.position[1] - self.radius == block_top:
                self.reverse_y()
                block.delete()
                break

            #Collides with bottom side
            if self.position[0] - self.radius <= block_right and self.position[0] + self.radius >= block_left\
                and self.position[1] + self.radius == block_bottom:
                self.reverse_y()
                block.delete()
                break
        

    