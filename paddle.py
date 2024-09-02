import random

from segment import Segment
from global_constants import PADDLE_SEGMENT_WIDTH, PADDLE_DIRECTION_NEGATION_VALUE, PADDLE_DIRECTION_MAINTAIN_VALUE


class Paddle:
    """Represents the paddle"""""

    def __init__(self, coordinates):
        self.segments = []
        self.makes_paddle(coordinates)

    def makes_paddle(self, initial_coordinates):
        """Makes the paddle from segments"""""
        for coord in initial_coordinates:
            self.segments.append(
                Segment(coordinate=coord, length=PADDLE_SEGMENT_WIDTH))

    def go_up(self):
        """Moves the paddle up by increasing the current ycor for each segment by 20"""""
        for seg in self.segments:
            seg.move()

    def go_down(self):
        """Moves the paddle up by decreasing the current ycor for each segment by 20"""""
        for seg in self.segments:
            seg.move(direction=PADDLE_DIRECTION_NEGATION_VALUE)

    def hit_ball(self, ball, x_direction):
        """Checks if the paddle hits the ball"""""
        if self.segments[0].distance(ball) <= 10:
            ball.bounce(x_direction=x_direction, y_direction=+1, increase_ball_speed=True)
        elif self.segments[1].distance(ball) <= 10:
            ball.bounce(x_direction=x_direction, y_direction=0, increase_ball_speed=True)
        elif self.segments[2].distance(ball) <= 10:
            ball.bounce(x_direction=x_direction, y_direction=-1, increase_ball_speed=True)

    def move(self, ball_ycor):
        """Moves the paddle automatically"""""
        ball_ycor_possible_ycors = [ball_ycor + 20, ball_ycor, ball_ycor - 20]

        if ball_ycor > 0:
            paddle_ycor = ball_ycor_possible_ycors[2]
        elif ball_ycor < 0:
            paddle_ycor = ball_ycor_possible_ycors[0]
        else:
            paddle_ycor = ball_ycor_possible_ycors[2]

        segments_positions = [(-380, paddle_ycor + 20), (-380, paddle_ycor), (-380, paddle_ycor - 20)]
        if random.randint(0, 15) == 0:
            for seg in self.segments:
                seg.goto(segments_positions[self.segments.index(seg)])
