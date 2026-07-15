import turtle
import random

turtle.colormode(255)  # Allows RGB values from 0-255
def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)

x = turtle.Turtle()

def loop(o):
    x.forward(10*o)
    x.color(random_color())
    x.right(90)
    x.color(random_color())
    x.forward(10*o)
    x.color(random_color())
    x.right(90)
    x.color(random_color())

for i in range(1 , 100):
    loop(i)
