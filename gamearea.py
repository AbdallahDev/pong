from turtle import Turtle, Screen


class GameArea:
    def __init__(self, window_width, widow_height):
        self.widow_width = window_width
        self.widow_height = widow_height
        self.ycor = 40 - (self.widow_height // 2)
        self.screen = Screen()
        self.setup_screen()
        self.draw_middle_line()

    def setup_screen(self):
        self.screen = Screen()
        self.screen.setup(width=self.widow_width, height=self.widow_height, startx=1)
        self.screen.bgcolor("black")
        self.screen.title("Pong Game")
        self.screen.tracer(False)

    def draw_middle_line(self):
        """draw the game area middle line"""
        while self.ycor < (self.widow_height // 2) - 40:
            news_turtle = Turtle()
            news_turtle.shape("square")
            news_turtle.color("white")
            news_turtle.penup()
            news_turtle.shapesize(stretch_wid=1, stretch_len=0.25)
            news_turtle.setposition(x=0, y=self.ycor)
            self.ycor += 40
            print(self.ycor)

        self.screen.update()

    def dont_exit(self):
        self.screen.exitonclick()
