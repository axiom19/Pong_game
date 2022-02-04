from turtle import Screen
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Score

screen = Screen()
screen.setup(width=900, height=720)
screen.title('Pong Game')
screen.bgcolor('black')
screen.tracer(0)

l_paddle = (-435, 0)
r_paddle = (430, 0)

paddle_left = Paddle(l_paddle)
paddle_right = Paddle(r_paddle)
ball = Ball()
score = Score()

screen.listen()
screen.onkeypress(paddle_left.up, 'Up')
screen.onkeypress(paddle_left.down, 'Down')
screen.onkeypress(paddle_right.up, 'w')
screen.onkeypress(paddle_right.down, 's')

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(ball.move_speed)
    ball.move()

    # detect collision with right paddle
    if ball.distance(paddle_right) < 60 and ball.xcor() > 410:
        ball.paddle_hit()

    # detect collision with left paddle
    if ball.distance(paddle_left) < 60 and ball.xcor() < -415:
        ball.paddle_hit()

    # detect collision with wall
    if ball.ycor() > 330 or ball.ycor() < -330:
        ball.bounce()

    # Keeping up with the scores
    if score.score1 == 10 or score.score2 == 10 and score.score1 > score.score2:
        game_is_on = False

    elif score.score1 == 10 or score.score2 == 10 and score.score1 < score.score2:
        game_is_on = False

    if ball.xcor() > 430:
        score.score1 += 1
        score.update_score()
        ball.restart()

    if ball.xcor() < -430:
        score.score2 += 1
        score.update_score()
        ball.restart()

if score.score1 > score.score2:
    score.update_score()
    score.goto(0, 0)
    score.write("Player 1 WINS !!!", False, 'center', ('Courier', 40, 'normal'))

if score.score1 < score.score2:
    score.update_score()
    score.goto(0, 0)
    score.write("Player 2 WINS !!!", False, 'center', ('Courier', 40, 'normal'))


screen.exitonclick()
