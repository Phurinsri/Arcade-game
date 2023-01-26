from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import ScoreBoard
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Arcade Game")
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = ScoreBoard()

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

game_on = True
while game_on:
    time.sleep(ball.ball_speed)
    ball.move()
    screen.update()

    # detect wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        # need to bounce
        ball.bounce_y()
    # detect paddle
    if (ball.distance(r_paddle) < 45 and 360 > ball.xcor() > 325) or (ball.distance(l_paddle) < 45 and -360 < ball.xcor() < -325):
        ball.bounce_x()
    # detect paddle missed
    if ball.xcor() > 370:
        ball.reset_ball()
        scoreboard.l_score()

    if ball.xcor() < -370:
        ball.reset_ball()
        scoreboard.r_score()

screen.exitonclick()
