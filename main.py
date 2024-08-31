# todo create segment class
# todo : create the paddle class
# todo : create the ball class
# todo : scoreboard class
import turtle

from arena import Arena


def game():
    t = turtle.Turtle()
    while True:
        t.color('red')


while True:
    arena = Arena()
    play = arena.play_game_prompt()
    if play == 'y':
        game()
    elif play == 'n':
        break
