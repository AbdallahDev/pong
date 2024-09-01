from segment import Segment
from global_constants import PADDLE_SEGMENT_WIDTH


class Paddle:
    """Represents the paddle"""""

    def __init__(self, coordinates):
        self.segments = []
        self.makes_paddle(coordinates)

    def makes_paddle(self, initial_coordinates):
        """Makes the paddle from segments"""""
        colors = ['red', 'blue', 'green']
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
            seg.move(direction=-1)

    def hit_ball(self, ball, x_direction):
        """Checks if the paddle hits the ball"""""
        if self.segments[0].distance(ball) <= 10:
            ball.bounce(x_direction=x_direction, y_direction=+1, increase_ball_speed=True)
        elif self.segments[1].distance(ball) <= 10:
            ball.bounce(x_direction=x_direction, y_direction=0, increase_ball_speed=True)
        elif self.segments[2].distance(ball) <= 10:
            ball.bounce(x_direction=x_direction, y_direction=-1, increase_ball_speed=True)
