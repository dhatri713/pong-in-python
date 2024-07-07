from turtle import Turtle
import random

COLOR = "white"
SHAPE = "circle"
STRETCH_LEN = 1
STRETCH_WID = 1
RIGHT = range(0, 400)
LEFT = range(0, -400)


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape(SHAPE)
        self.shapesize(stretch_wid=STRETCH_WID, stretch_len=STRETCH_LEN)
        self.color(COLOR)
        self.penup()
        self.move_y = 10
        self.move_x = 10
        self.speed_val = 5
        self.move_speed = 0.1

    def move(self):
        new_x = self.xcor() + self.move_x
        new_y = self.ycor() + self.move_y
        self.goto(new_x, new_y)

    def bounce_wall(self):
        self.move_y *= -1

    def bounce_paddle(self):
        self.move_x *= -1
        self.move_speed *= 0.9

    def reset(self):
        self.goto(0, 0)
        self.move_x *= -1
        self.move_speed = 0.1

    def reset_speed(self):
        self.speed_val += 1
        self.speed(self.speed_val)
