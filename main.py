import time
import turtle
import random

WIDTH = 2000
HEIGHT = 1600


def setup_turtles(num=5):
    turtles = []
    for i in range(num):
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        t.shape("turtle")
        t.color("red")
        x, y = random.randint(int(-WIDTH / 4), int(WIDTH / 4)), \
               random.randint(int(-HEIGHT / 4), int(HEIGHT / 4))
        t.goto(x, y)
        t.left(90)
        t.showturtle()
        turtles.append(t)

    return turtles


def setup_robots(num=3):
    robots = []
    for i in range(num):
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        t.shape("arrow")
        t.color("blue")
        x, y = random.randint(int(-WIDTH / 4), int(WIDTH / 4)), \
               random.randint(int(-HEIGHT / 4), int(HEIGHT / 4))
        t.goto(x, y)
        t.left(90)
        t.showturtle()
        robots.append(t)

    return robots


if __name__ == '__main__':
    turtle.title("DSD")

    screen = turtle.Screen()
    screen.setup(WIDTH, HEIGHT)

    turtles = setup_turtles(6)
    robots = setup_robots(3)

    while True:
        for t in turtles:
            t.forward(1)
        for r in robots:
            t = random.choice(turtles)
            r.speed(1)
            r.goto(t.pos())
