from turtle import Turtle

from global_constants import SEGMENT_STEPS, SEGMENT_CEILING_HIT_POINT, SEGMENT_FLOOR_HIT_POINT, SEGMENT_SHAPE, \
    SEGMENT_COLOR, SEGMENT_DEFAULT_WIDTH, SEGMENT_DEFAULT_LENGTH, SEGMENT_DEFAULT_DIRECTION


class Segment(Turtle):
    """Represents all the segments in the game, like the paddle segments or the net or the ball as one segment"""""

    def __init__(self, coordinate, width=SEGMENT_DEFAULT_WIDTH, length=SEGMENT_DEFAULT_LENGTH):
        super().__init__()
        self.shape(SEGMENT_SHAPE)
        self.color(SEGMENT_COLOR)
        self.penup()
        self.shapesize(stretch_wid=width, stretch_len=length)
        self.goto(coordinate)

    def move(self, direction=SEGMENT_DEFAULT_DIRECTION):
        """Moves the segment"""""
        # if the direction -1 that means the segment should moves up, otherwise it should moves down
        self.goto(x=self.xcor(), y=self.ycor() + (direction * SEGMENT_STEPS))
