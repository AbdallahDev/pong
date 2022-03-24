from gamearea import GameArea
from paddle import Paddle
from turtle import Screen

screen = Screen()
game_area = GameArea(window_width=1400, widow_height=800)

paddle1 = Paddle()
game_area.dont_exit()
