import random

from segment import Segment
from global_constants import PADDLE_SEGMENT_WIDTH, PADDLE_DIRECTION_NEGATION_VALUE, PADDLE_DIRECTION_MAINTAIN_VALUE, \
    PADDLE_CHANCE_DOWN_RANGE, PADDLE_CHANCE_VALUE, PADDLE_SEGMENTS_YCOR_SPACING, PADDLE_CHANGING_DIRECTION_YCOR_VALUE, \
    PADDLE_SEGMENTS_YCOR_LIMIT, BALL_DISTANCE, POSITIVE_Y_DIRECTION, NEUTRAL_Y_DIRECTION, NEGATIVE_Y_DIRECTION


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
        if self.segments[0].distance(ball) <= BALL_DISTANCE:
            ball.bounce(x_direction=x_direction, y_direction=POSITIVE_Y_DIRECTION, increase_ball_speed=True)
        elif self.segments[1].distance(ball) <= BALL_DISTANCE:
            ball.bounce(x_direction=x_direction, y_direction=NEUTRAL_Y_DIRECTION, increase_ball_speed=True)
        elif self.segments[2].distance(ball) <= BALL_DISTANCE:
            ball.bounce(x_direction=x_direction, y_direction=NEGATIVE_Y_DIRECTION, increase_ball_speed=True)

    def move(self, ball_ycor, paddle_movement_chance_up_range):
        """Moves the paddle automatically"""""
        paddle_segment_start_ycor = [ball_ycor + PADDLE_SEGMENTS_YCOR_SPACING, ball_ycor,
                                     ball_ycor - PADDLE_SEGMENTS_YCOR_SPACING]

        if ball_ycor > PADDLE_CHANGING_DIRECTION_YCOR_VALUE:
            paddle_ycor = paddle_segment_start_ycor[2]
        elif ball_ycor < PADDLE_CHANGING_DIRECTION_YCOR_VALUE:
            paddle_ycor = paddle_segment_start_ycor[0]
        else:
            paddle_ycor = paddle_segment_start_ycor[2]

        segments_positions = [(-PADDLE_SEGMENTS_YCOR_LIMIT, paddle_ycor + PADDLE_SEGMENTS_YCOR_SPACING),
                              (-PADDLE_SEGMENTS_YCOR_LIMIT, paddle_ycor),
                              (-PADDLE_SEGMENTS_YCOR_LIMIT, paddle_ycor - PADDLE_SEGMENTS_YCOR_SPACING)]

        if random.randint(PADDLE_CHANCE_DOWN_RANGE, paddle_movement_chance_up_range) == PADDLE_CHANCE_VALUE:
            for seg in self.segments:
                seg.goto(segments_positions[self.segments.index(seg)])
