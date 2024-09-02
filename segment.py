from turtle import Turtle

from global_constants import SEGMENT_STEPS, SEGMENT_CEILING_HIT_POINT, SEGMENT_FLOOR_HIT_POINT


class Segment(Turtle):
    """Represents all the segments in the game, like the paddle segments or the net or the ball as one segment"""""

    def __init__(self, coordinate, width=1, length=1, color='black'):
        super().__init__()
        self.shape('square')
        self.color(color)
        self.penup()
        self.shapesize(stretch_wid=width, stretch_len=length)
        self.goto(coordinate)

    def move(self, direction=1):
        """Moves the segment"""""
        # if the direction -1 that means the segment should moves up, otherwise it should moves down
        self.goto(x=self.xcor(), y=self.ycor() + (direction * SEGMENT_STEPS))

