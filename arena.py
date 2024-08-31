import turtle

from global_constants import SCREEN_WIDTH, SCREEN_HEIGHT, WINDOW_TITLE, PROMPT_TITLE, PROMPT_TXT


class Arena:
    def __init__(self):
        turtle.title(WINDOW_TITLE)
        turtle.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)

    def play_game_prompt(self):
        return turtle.textinput(title=PROMPT_TITLE, prompt=PROMPT_TXT)
