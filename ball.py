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
        v_y = 5

        self.velocity = [v_x, v_y]

    def draw(self):
        x1, y1 = self.position[0] - self.radius, self.position[1] - self.radius
        x2, y2 = self.position[0] + self.radius, self.position[1] + self.radius
        self.oval = self.canvas.create_oval(x1, y1, x2, y2, fill = self.color)
    
    def move(self):
        self.position = self.velocity + self.position
        self.canvas.move(self.oval, self.velocity[0], self.velocity[1])


    def collide(self):
        """Encodes what happens during a collision between the platform and the ball"""
        self.velocity[1] *= -1


def check(platform1, ball1):
    """Checks ball position and changes velocity depending on whether the ball has collided with the
    walls or platform"""
    dx = platform1.position[0] - ball1.position[0]
    dy = platform1.position[1] - ball1.position[1]
    r = np.sqrt(dx**2 + dy**2)

    if ball1.position[0] >= platform1.x1 - ball1.radius and ball1.position[1] == platform1.y1 \
        and ball1.position[0] <= platform1.x2 + ball1.radius:
        ball1.collide()

    if ball1.position[0] >= canvas_width - ball1.radius:
        #If ball all the way to the right hand side
        ball1.velocity[0] *= -1 

    if ball1.position[0] <= ball1.radius:
        #If ball all the way to the left
        ball1.velocity[0] *= -1

    if ball1.position[1] <= ball1.radius:
        #If ball is all the way at the top
        ball1.velocity[1] *= -1

    if canvas_height - ball1.position[1] <= r:
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
        if ball1.position[0] + ball1.radius == block_left and ball1.position[1] + ball1.radius >= block_bottom\
              and ball1.position[1] - ball1.radius <= block_top:
            ball1.velocity[0] *= -1
                
        #Collides with right hand side
        if ball1.position[0] - ball1.radius == block_right and ball1.position[1] + ball1.radius >= block_bottom\
              and ball1.position[1] - ball1.radius <= block_top:
            ball1.velocity[0] *= -1

        #Collides with top side
        if ball1.position[0] - ball1.radius <= block_right and ball1.position[0] + ball1.radius >= block_left\
              and ball1.position[1] - ball1.radius == block_top:
            ball1.velocity[1] *= -1

        #Collides with bottom side
        if ball1.position[0] - ball1.radius <= block_right and ball1.position[0] + ball1.radius >= block_left\
              and ball1.position[1] + ball1.radius == block_bottom:
            ball1.velocity[1] *= -1
        

    