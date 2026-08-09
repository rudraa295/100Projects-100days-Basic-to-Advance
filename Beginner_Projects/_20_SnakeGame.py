import time
import random
from turtle import Turtle, Screen

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

turtle_positions = [(0, 0), (-20, 0), (-40, 0)]
segment = []

food = Turtle()
food.shape("circle")
food.color("blue")
food.penup()
food.speed(0)

def move_food():
    x = random.randint(-14, 14) * 20
    y = random.randint(-14, 14) * 20
    food.goto(x, y)

for position in turtle_positions:
    new_turtle = Turtle("square")
    new_turtle.penup()
    new_turtle.color("white")
    new_turtle.goto(position)
    segment.append(new_turtle)

def left():
    segment[0].left(90)

def right():
    segment[0].right(90)

screen.listen()
screen.onkey(left, "Left")
screen.onkey(right, "Right")

move_food()

while True:
    screen.update()
    time.sleep(0.1)

    for seg_num in range(len(segment) - 1, 0, -1):
        new_x = segment[seg_num - 1].xcor()
        new_y = segment[seg_num - 1].ycor()
        segment[seg_num].goto(new_x, new_y)

    segment[0].forward(20)

    x_cor = segment[0].xcor()
    y_cor = segment[0].ycor()

    if x_cor > 290 or x_cor < -290:
        segment[0].goto(-x_cor, y_cor)
    elif y_cor < -290 or y_cor > 290:
        segment[0].goto(x_cor, -y_cor)

    if segment[0].distance(food) < 20:
        move_food()

        new_segment = Turtle("circle")
        new_segment.penup()
        new_segment.color("red")
        segment.append(new_segment)