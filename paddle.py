from turtle import Turtle, Screen


class Paddle(Turtle):
    def __init__(self):
        super().__init__()
        self.screen = Screen()
        self.draw_paddle()

    def draw_paddle(self):
        self.pendown()
        self.shape("square")
        self.color("blue")
        self.setposition(x=-50, y=0)
        self.screen.update()
