from turtle import Turtle, Screen


class Paddle(Turtle):
    def __init__(self):
        super().__init__()
        self.screen = Screen()
        self.window_width = self.screen.window_width()
        self.window_height = self.screen.window_height()
        self.xcor = 20 - (self.screen.window_width() // 2)
        self.ycor = (self.screen.window_height() // 2) - 40
        self.draw_paddle()

    def draw_paddle(self):
        """draw the paddle"""
        self.penup()
        self.shape("square")
        self.shapesize(stretch_wid=2, stretch_len=0.5)
        self.color("white")
        self.setposition(x=self.xcor, y=self.ycor)
        self.screen.update()
