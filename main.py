from turtle import Screen, Turtle

from gamearea import GameArea

screen = Screen()
screen.setup(width=1400, height=800, startx=1)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(False)

game_area = GameArea(screen.window_height())
print(game_area.ycor)

screen.update()
screen.exitonclick()
