from turtle import Turtle


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.score1 = 0
        self.score2 = 0
        self.scoreboard_1()
        self.scoreboard_2()
        self.goto(0, 350)
        self.seth(270)
        while self.ycor() != -350:
            self.centre_line()

    def centre_line(self):
        self.pencolor('white')
        self.pendown()
        self.fd(50)
        self.penup()
        self.fd(20)

    def scoreboard_1(self):
        self.color('white')
        self.goto(x=-25, y=305)
        self.write(f'{self.score1}', move=False, align='center', font=('Courier', 30, 'normal'))

    def scoreboard_2(self):
        self.color('white')
        self.goto(x=25, y=305)
        self.write(f'{self.score2}', move=False, align='center', font=('Courier', 30, 'normal'))

    def update_score(self):
        self.clear()
        self.goto(0, 350)
        self.seth(270)
        while self.ycor() != -350:
            self.centre_line()
        self.scoreboard_1()
        self.scoreboard_2()

