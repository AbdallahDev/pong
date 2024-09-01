from turtle import Turtle

from global_constants import BALL_SHAPE, STRETCH_WID, STRETCH_LEN


class Ball(Turtle):
    """"Represents the ball movement"""

    def __init__(self):
        super().__init__()
        self.penup()
        self.shape(BALL_SHAPE)
        self.x_direction = 1
        self.y_direction = 1
        self.shapesize(stretch_wid=STRETCH_WID,
                       stretch_len=STRETCH_LEN)

    def move(self):
        """"Moves the ball"""
        self.goto(
            self.xcor() + (self.x_direction * 2),
            self.ycor() + (self.y_direction * 1),
        )
        print(self.x_direction, self.y_direction)

    def bounce(self, x_direction=1, y_direction=1):
        """"Bounces the ball"""
        self.x_direction = x_direction
        self.y_direction = y_direction
