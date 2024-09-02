import turtle

turtle.listen()


def test():
    print('press')


turtle.onkeypress(fun=test, key="Up")
turtle.mainloop()