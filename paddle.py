from segment import Segment
from global_constants import PADDLE_SEGMENT_WIDTH


class Paddle:
    """Represents the paddle"""""

    def __init__(self, coordinates):
        self.segments = []
        self.makes_paddle(coordinates)

    def makes_paddle(self, initial_coordinates):
        """Makes the paddle from segments"""""
        for coord in initial_coordinates:
            self.segments.append(Segment(coordinate=coord, length=PADDLE_SEGMENT_WIDTH))

    def go_up(self):
        """Moves the paddle up by increasing the current ycor for each segment by 20"""""
        for seg in self.segments:
            seg.move()

    def go_down(self):
        """Moves the paddle up by decreasing the current ycor for each segment by 20"""""
        for seg in self.segments:
            seg.move(direction=-1)
