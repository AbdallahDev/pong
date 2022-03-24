from turtle import Turtle, Screen


class Paddle(Turtle):
    def __init__(self, xcor_determiner, ycor_determiner):
        super().__init__()
        self.screen = Screen()
        self.window_width = self.screen.window_width()
        self.window_height = self.screen.window_height()
        self.xcor_determiner = xcor_determiner
        self.ycor_determiner = ycor_determiner
        self.xcor = ((self.screen.window_width() // 2) - 40) * self.xcor_determiner
        self.ycor = ((self.screen.window_height() // 2) - 60) * self.ycor_determiner
        self.draw_paddle()

    def draw_paddle(self):
        """draw the paddle"""
        self.penup()
        self.shape("square")
        self.shapesize(stretch_wid=3.5, stretch_len=1)
        self.color("white")
        self.setposition(x=self.xcor, y=self.ycor)
        self.screen.update()
        print(self.screen.window_width(), self.screen.window_height())
