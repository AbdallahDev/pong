import turtle

import keyboard

turtle.listen()
while True:
    if keyboard.is_pressed("n") and keyboard.is_pressed("m"):
        print("n and m pressed")
