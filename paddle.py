from turtle import Turtle

l_paddle = (-435, 0)
r_paddle = (430, 0)
UP = 90
DISTANCE = 20


class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.color('white')
        self.shape('square')
        self.penup()
        self.speed(0)
        self.shapesize(stretch_wid=1, stretch_len=5)
        self.goto(position)
        self.seth(UP)

    def up(self):
        self.fd(DISTANCE)

    def down(self):
        self.bk(DISTANCE)
