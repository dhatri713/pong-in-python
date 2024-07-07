from turtle import Turtle

COLOR = "white"
SHAPE = "square"
STRETCH_LEN = 1
STRETCH_WID = 5
MOVE_DISTANCE = 20


class Paddle(Turtle):
    def __init__(self, coordinates):
        super().__init__()
        self.shape(SHAPE)
        self.color(COLOR)
        self.shapesize(stretch_wid=STRETCH_WID, stretch_len=STRETCH_LEN)
        self.penup()
        self.goto(coordinates)

    def go_up(self):
        new_y = self.ycor() + MOVE_DISTANCE
        new_pos = (self.xcor(), new_y)
        self.goto(new_pos)

    def go_down(self):
        new_y = self.ycor() - MOVE_DISTANCE
        new_pos = (self.xcor(), new_y)
        self.goto(new_pos)
