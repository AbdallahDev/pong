import turtle


class PlayingMode:
    """Represents the play mode, single or multiple"""""

    def __init__(self):
        self.single_mode = True
        self.set_playing_mode()

    def set_playing_mode(self):
        """sets the playing mode, single player or multiple players"""""
        mode = int(turtle.textinput(title="Playing Mode", prompt="Chose the playing mode (1:single,2:two): ").lower())

        if mode == 1:
            self.single_mode = True
        elif mode == 2:
            self.single_mode = False
