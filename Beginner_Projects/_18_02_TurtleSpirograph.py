import turtle
import random

t = turtle.Turtle()
turtle.colormode(255)

radius = 100

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)

def draw_circle():
    t.color(random_color())
    t.circle(100)

t.speed("fastest")

for i in range(360):
    draw_circle()
    t.forward(2 * 3.14 * radius / 360)
    t.left(3)

turtle.done()