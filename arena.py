import turtle

from global_constants import SCREEN_WIDTH, SCREEN_HEIGHT, WINDOW_TITLE, NET_COORDINATES, NET_SEGMENT_WIDTH, \
    NET_SEGMENT_LENGTH
from segment import Segment


class Arena:
    """Represents the game arena"""""

    def __init__(self):
        turtle.title(WINDOW_TITLE)
        turtle.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
        self.draw_net()

    def draw_net(self):
        """Draws the net in the middle of the arena"""""
        for coord in NET_COORDINATES:
            Segment(coord, width=NET_SEGMENT_WIDTH, length=NET_SEGMENT_LENGTH)
