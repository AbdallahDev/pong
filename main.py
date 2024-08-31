# todo create segment class
# todo : create the paddle class
# todo : create the ball class
# todo : scoreboard class
import time
import turtle

from arena import Arena
from global_constants import PROMPT_TITLE, PROMPT_TXT


def game():
    turtle.tracer(0)
    Arena()
    t = turtle.Turtle()
    while True:
        t.color('red')
        turtle.update()
        time.sleep(1)


while True:
    play = turtle.textinput(title=PROMPT_TITLE, prompt=PROMPT_TXT)
    if play == 'y':
        game()
    elif play == 'n':
        break
