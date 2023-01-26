from turtle import Turtle
import random


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.shapesize(stretch_wid=1, stretch_len=1)
        self.color("white")
        self.penup()
        self.x_move = 10
        self.y_move = random.randint(0,10)
        self.ball_speed = 0.1

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.y_move *= -1
        self.ball_speed *= 0.8

    def bounce_x(self):
        self.x_move *= -1
        self.ball_speed *= 0.8

    def reset_ball(self):
        self.ball_speed = 0.1
        self.goto(0, 0)
        self.bounce_x()
        self.y_move = random.randint(0, 10)


