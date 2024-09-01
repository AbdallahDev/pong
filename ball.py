from turtle import Turtle

from global_constants import BALL_SHAPE


class Ball(Turtle):
    """"Represents the ball movement"""

    def __init__(self):
        super().__init__()
        self.penup()
        self.shape(BALL_SHAPE)
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)

    def move(self):
        """"moves the ball"""
        pass
