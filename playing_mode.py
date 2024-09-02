import turtle
from global_constants import SINGLE_MODE_DEFAULT_VALUE, SINGLE_MODE_NEGATE_VALUE, PLAYING_MODE_PROMPT_TITLE, \
    PLAYING_MODE_PROMPT_TXT, PLAYING_MODE_FIRST_INDX, PLAYING_MODE_SECOND_INDX


class PlayingMode:
    """Represents the play mode, single or multiple"""""

    def __init__(self):
        self.single_mode = SINGLE_MODE_DEFAULT_VALUE
        self.set_playing_mode()

    def set_playing_mode(self):
        """sets the playing mode, single player or multiple players"""""
        mode = int(turtle.textinput(title=PLAYING_MODE_PROMPT_TITLE,
                                    prompt=PLAYING_MODE_PROMPT_TXT).lower())

        if mode == PLAYING_MODE_FIRST_INDX:
            self.single_mode = SINGLE_MODE_DEFAULT_VALUE
        elif mode == PLAYING_MODE_SECOND_INDX:
            self.single_mode = SINGLE_MODE_NEGATE_VALUE
