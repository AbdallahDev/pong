from turtle import Turtle

from global_constants import BALL_SHAPE, STRETCH_WID, STRETCH_LEN, BALL_CEILING_HIT_LIMIT, BALL_FLOOR_HIT_LIMIT


class Ball(Turtle):
    """"Represents the ball movement"""""

    def __init__(self):
        super().__init__()
        self.penup()
        self.shape(BALL_SHAPE)
        self.x_direction = 1
        self.y_direction = 1
        self.shapesize(stretch_wid=STRETCH_WID,
                       stretch_len=STRETCH_LEN)

    def move(self):
        """"Moves the ball"""""
        self.goto(
            self.xcor() + (self.x_direction * 2),
            self.ycor() + (self.y_direction * 1),
        )
        self.check_wall_hit()

    def bounce(self, x_direction=1, y_direction=1):
        """"Bounces the ball"""""
        self.x_direction = x_direction
        self.y_direction = y_direction

        print(self.x_direction, self.y_direction)

    def check_wall_hit(self):
        """Check if the ball hits the wall, and if that happens it bounces the ball"""""
        if self.ycor() > BALL_CEILING_HIT_LIMIT:
            self.bounce(x_direction=self.x_direction, y_direction=-1)

        if self.ycor() < BALL_FLOOR_HIT_LIMIT:
            self.bounce(x_direction=self.x_direction, y_direction=1)
