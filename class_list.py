import tkinter as tk
import numpy as np

canvas_width = 800
canvas_height = 800

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
        self.canvas.move(self.rectangle, -1*self.movement_speed, 0)
        self.position[0] -= self.movement_speed
        self.x1 -= self.movement_speed
        self.x2 -= self.movement_speed

    def move_right(self, event):
        self.canvas.move(self.rectangle, self.movement_speed, 0)
        self.position[0] += self.movement_speed
        self.x1 += self.movement_speed
        self.x2 += self.movement_speed

class Ball:
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
        v_x = np.random.uniform(-5,5)
        v_y = 2

        self.velocity = [v_x, v_y]

    def draw(self):
        x1, y1 = self.position[0] - self.radius, self.position[1] - self.radius
        x2, y2 = self.position[0] + self.radius, self.position[1] + self.radius
        self.oval = self.canvas.create_oval(x1, y1, x2, y2, fill = self.color)
    
    def move(self):
        self.position = self.velocity + self.position
        self.canvas.move(self.oval, self.velocity[0], self.velocity[1])

def collide(platform1, ball1):
    """Encodes what happens during a collision between the platform and the ball"""
    ball1.velocity[1] *= -1

def check(platform1, ball1):
    """Checks ball position and changes velocity depending on whether the ball has collided with the
    walls or platform"""
    dx = platform1.position[0] - ball1.position[0]
    dy = platform1.position[1] - ball1.position[1]
    r = np.sqrt(dx**2 + dy**2)

    if ball1.position[0] >= platform1.x1 - ball1.radius and ball1.position[1] == platform1.y1 \
        and ball1.position[0] <= platform1.x2 + ball1.radius:
        
        collide(platform1, ball1)

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
