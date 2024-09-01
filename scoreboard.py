# todo : increases the score
# todo: finish the game after the 10 points
from turtle import Turtle

from global_constants import DEFAULT_SCORE, SCORE_INCREASE_VALUE, SCORE_TXT, SCORE_TXT_ALIGNMENT, SCORE_TXT_FONT, \
    SCORE_TXT_DEFAULT_POSITION


class ScoreBoard(Turtle):
    """Represents the ScoreBoard"""""

    def __init__(self, position):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.score_position = position
        self.goto(self.score_position)
        self.score = DEFAULT_SCORE
        self.update_score()

    def update_score(self):
        """Updates the score on the screen"""""
        self.score += SCORE_INCREASE_VALUE
        self.write_score_txt()

    def write_score_txt(self):
        self.clear()
        self.write(arg=self.score, align=SCORE_TXT_ALIGNMENT, font=SCORE_TXT_FONT)
