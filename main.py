# todo : create the paddle class
# todo : create the ball class
# todo : scoreboard class
import time
import turtle

from arena import Arena
from ball import Ball
from global_constants import (PROMPT_TITLE, PROMPT_TXT, R_PADDLE_COORDINATES,
                              L_PADDLE_COORDINATES, R_SCORE_POSITION, L_SCORE_POSITION, KEYS)
from paddle import Paddle
from scoreboard import ScoreBoard


def game():
    turtle.tracer(0)
    turtle.listen()

    Arena()
    ball = Ball()

    r_scoreboard = ScoreBoard(position=R_SCORE_POSITION)
    r_paddle = Paddle(coordinates=R_PADDLE_COORDINATES)

    l_scoreboard = ScoreBoard(position=L_SCORE_POSITION)
    l_paddle = Paddle(coordinates=L_PADDLE_COORDINATES)

    turtle.onkeypress(fun=r_paddle.go_up, key=KEYS[0])
    turtle.onkeypress(fun=r_paddle.go_down, key=KEYS[1])
    turtle.onkeypress(fun=l_paddle.go_up, key=KEYS[2])
    turtle.onkeypress(fun=l_paddle.go_down, key=KEYS[3])

    end_game = False
    while not end_game:
        if not ball.move(r_paddle=r_paddle, l_paddle=l_paddle, l_scoreboard=l_scoreboard, r_scoreboard=r_scoreboard):
            end_game = True

        turtle.update()
        time.sleep(0.01)


while True:
    play = turtle.textinput(title=PROMPT_TITLE, prompt=PROMPT_TXT)
    # play = 'y'
    if play == 'y':
        turtle.clearscreen()
        game()
    elif play == 'n':
        break
