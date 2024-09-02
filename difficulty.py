import turtle
from global_constants import BALL_INCREASE_SPEED_VALUES, DIFFICULTY_PROMPT_MSG, DIFFICULTY_PROMPT_TITLE, \
    DIFFICULTY_PROMPT_MSG_ERROR, PADDLE_CHANCE_DEFAULT_VALUE, PADDLE_CHANCE_LEVELS_VALUES, DIFFICULTY_LEVELS_VALUES


class Difficulty:
    """sets the game difficulty and based on it the speed of the snake decided"""""

    def __init__(self):
        super().__init__()
        # self.ball_increasing_speed = BALL_INCREASE_SPEED_VALUES[0]
        self.paddle_movement_chance = PADDLE_CHANCE_DEFAULT_VALUE
        self.set_difficulty()

    def set_difficulty(self, prompt_msg=DIFFICULTY_PROMPT_MSG):
        """sets the game difficulty based on the user input."""""
        difficulty = int((
            turtle.
            textinput(DIFFICULTY_PROMPT_TITLE, f"{prompt_msg}").lower()))
        self.set_speed(difficulty_par=difficulty)

    def set_speed(self, difficulty_par):
        """based on the chosen difficulty of the snake speed will be set"""""
        if difficulty_par == DIFFICULTY_LEVELS_VALUES[0]:
            self.paddle_movement_chance = PADDLE_CHANCE_LEVELS_VALUES[0]
        elif difficulty_par == DIFFICULTY_LEVELS_VALUES[1]:
            self.paddle_movement_chance = PADDLE_CHANCE_LEVELS_VALUES[1]
        elif difficulty_par == DIFFICULTY_LEVELS_VALUES[2]:
            self.paddle_movement_chance = PADDLE_CHANCE_LEVELS_VALUES[2]
        else:
            self.set_difficulty(prompt_msg=DIFFICULTY_PROMPT_MSG_ERROR)
