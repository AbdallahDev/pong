from gamearea import GameArea
from paddle import Paddle

game_area = GameArea(window_width=1000, widow_height=600)

paddle1 = Paddle(xcor_determiner=-1, ycor_determiner=1)
paddle2 = Paddle(xcor_determiner=1, ycor_determiner=-1)
game_area.dont_exit()
