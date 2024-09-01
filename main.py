# todo : create the paddle class
# todo : create the ball class
# todo : scoreboard class
import time
import turtle

from arena import Arena
from global_constants import PROMPT_TITLE, PROMPT_TXT, R_PADDLE_COORDINATES, L_PADDLE_COORDINATES
from paddle import Paddle


def game():
    turtle.tracer(0)
    turtle.listen()

    Arena()
    r_paddle = Paddle(coordinates=R_PADDLE_COORDINATES)
    l_paddle = Paddle(coordinates=L_PADDLE_COORDINATES)

    turtle.onkeypress(fun=r_paddle.go_up, key='Up')
    turtle.onkeypress(fun=r_paddle.go_down, key='Down')
    turtle.onkeypress(fun=l_paddle.go_up, key='w')
    turtle.onkeypress(fun=l_paddle.go_down, key='s')

    while True:
        turtle.update()
        time.sleep(0.01)


while True:
    # play = turtle.textinput(title=PROMPT_TITLE, prompt=PROMPT_TXT)
    play = 'y'
    if play == 'y':
        game()
    elif play == 'n':
        break
