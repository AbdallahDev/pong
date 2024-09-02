import random
import time
import turtle

from arena import Arena
from ball import Ball
from global_constants import (PROMPT_TITLE, PROMPT_TXT, R_PADDLE_COORDINATES,
                              L_PADDLE_COORDINATES, R_SCORE_POSITION, L_SCORE_POSITION, KEYS, SLEEP_TIME,
                              TRACER_DEFAULT_VALUE, PLAY_ACCEPT_INPUT, PLAY_DENY_INPUT)
from paddle import Paddle
from scoreboard import ScoreBoard
from difficulty import Difficulty
from playing_mode import PlayingMode


def game():
    turtle.tracer(TRACER_DEFAULT_VALUE)

    playing_mode = PlayingMode()
    single_mode = playing_mode.single_mode
    difficulty = Difficulty()
    Arena()
    ball = Ball(difficulty.ball_increasing_speed)

    r_scoreboard = ScoreBoard(position=R_SCORE_POSITION)
    l_scoreboard = ScoreBoard(position=L_SCORE_POSITION)

    r_paddle = Paddle(coordinates=R_PADDLE_COORDINATES)
    l_paddle = Paddle(coordinates=L_PADDLE_COORDINATES)

    turtle.listen()
    turtle.onkeypress(fun=r_paddle.go_up, key=KEYS[0])
    turtle.onkeypress(fun=r_paddle.go_down, key=KEYS[1])
    if not single_mode:
        turtle.onkeypress(fun=l_paddle.go_up, key=KEYS[2])
        turtle.onkeypress(fun=l_paddle.go_down, key=KEYS[3])

    end_game = False
    while not end_game:
        if not ball.move(r_paddle=r_paddle, l_paddle=l_paddle, l_scoreboard=l_scoreboard, r_scoreboard=r_scoreboard):
            end_game = True

        if single_mode:
            l_paddle.move(ball.ycor())
        turtle.update()
        time.sleep(SLEEP_TIME)


while True:
    play = turtle.textinput(title=PROMPT_TITLE, prompt=PROMPT_TXT).lower()
    if play == PLAY_ACCEPT_INPUT:
        turtle.clearscreen()
        game()
    elif play == PLAY_DENY_INPUT:
        break
