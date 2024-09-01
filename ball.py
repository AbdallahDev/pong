from turtle import Turtle

from global_constants import BALL_SHAPE, BALL_STRETCH_WID, BALL_STRETCH_LEN, BALL_CEILING_HIT_LIMIT, \
    BALL_FLOOR_HIT_LIMIT, BALL_STEPS, RIGHT_GOAL_HIT, LEFT_GOAL_HIT, BALL_DIRECTION_DEFAULT_VALUE


class Ball(Turtle):
    """"Represents the ball movement"""""

    def __init__(self):
        super().__init__()
        self.penup()
        self.speed = BALL_STEPS
        self.shape(BALL_SHAPE)
        self.x_direction = BALL_DIRECTION_DEFAULT_VALUE
        self.y_direction = BALL_DIRECTION_DEFAULT_VALUE
        self.shapesize(stretch_wid=BALL_STRETCH_WID,
                       stretch_len=BALL_STRETCH_LEN)

    def move(self):
        """"Moves the ball"""""
        self.goto(
            self.xcor() + (self.x_direction * self.speed),
            self.ycor() + (self.y_direction * self.speed),
        )
        self.check_wall_hit()
        self.check_goal_conceded()

    def bounce(self, x_direction, y_direction, increase_ball_speed=False):
        """"Bounces the ball and increase the ball speed"""""
        # ball speed will increase if the ball hits the paddle
        self.increase_speed(increase_speed=increase_ball_speed)
        self.x_direction = x_direction
        self.y_direction = y_direction

    def check_wall_hit(self):
        """Check if the ball hits the wall, and if that happens it bounces the ball"""""
        if self.ycor() > BALL_CEILING_HIT_LIMIT or self.ycor() < BALL_FLOOR_HIT_LIMIT:
            # I'll negate the y direction to bounce the ball from the wall
            self.y_direction *= -1
            self.bounce(x_direction=self.x_direction, y_direction=self.y_direction)

    def check_goal_conceded(self):
        """Checks if the goal has been conceded, then reposition it to the center"""""
        # I'll negate the x direction to negate its direction after it reposition
        if self.xcor() > RIGHT_GOAL_HIT or self.xcor() < LEFT_GOAL_HIT:
            self.x_direction *= -1
            self.center_reposition()
            self.bounce(x_direction=self.x_direction, y_direction=self.y_direction)

    def center_reposition(self):
        """It will respawn the ball from the center, and reset the ball speed to default value"""""
        self.speed = BALL_STEPS
        self.goto(x=0, y=0)

    def increase_speed(self, increase_speed=True):
        """Increases the ball speed"""
        if increase_speed:
            self.speed += 0.2
