from turtle import Turtle

from global_constants import DEFAULT_SCORE, SCORE_INCREASE_VALUE, SCORE_TXT_ALIGNMENT, SCORE_TXT_FONT, \
    GAME_OVER_TXT, GAME_OVER_ALIGNMENT, GAME_OVER_FONT, GAME_OVER_COLOR, GAME_OVER_POSITION


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
        """Updates the score value"""
        self.score += SCORE_INCREASE_VALUE
        self.write_score_txt()
        if self.game_over():
            return True

    def write_score_txt(self):
        """Writes the score on the screen"""
        self.clear()
        self.write(arg=self.score, align=SCORE_TXT_ALIGNMENT, font=SCORE_TXT_FONT)

    def game_over(self):
        """checks if the score reached 10"""
        if self.score == 10:
            self.goto(GAME_OVER_POSITION)
            self.color(GAME_OVER_COLOR)
            self.write(arg=GAME_OVER_TXT, align=GAME_OVER_ALIGNMENT, font=GAME_OVER_FONT)
            return True
