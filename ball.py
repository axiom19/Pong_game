from turtle import Turtle
import random

SPEED = 3


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color('red')
        self.penup()
        self.x_move = SPEED
        self.y_move = SPEED
        self.move_speed = 0.01

    def paddle_hit(self):
        self.x_move *= -1
        self.move_speed *= 0.8

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce(self):
        self.y_move *= -1

    def restart(self):
        self.goto(0, 0)
        self.paddle_hit()
        self.move_speed = 0.01
