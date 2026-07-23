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

t = Turtle()
t.shape("square")
t.color("blue")
t.penup()
t.speed(0)

width = screen.window_width() // 2
height = screen.window_height() // 2

num_points = 100

def food():
    x = random.randint(-14, 14) * 20
    y = random.randint(-14, 14) * 20
    t.goto(x, y)


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


while True:
    food()
    game_on = True
    while game_on:
        screen.update()
        time.sleep(0.1)
        for seg_num in range(len(segment)-1, 0, -1):
            new_x = segment[seg_num - 1].xcor()
            new_y = segment[seg_num - 1].ycor()
            segment[seg_num].goto(new_x, new_y)

        segment[0].forward(10)
        x_cor = segment[0].xcor()
        y_cor = segment[0].ycor()

        if x_cor >290 or x_cor<-290:
            segment[0].goto(-x_cor, y_cor)
        elif y_cor <-290 or y_cor>290:
            segment[0].goto(x_cor, -y_cor)
        if x_cor==t.xcor() and y_cor==t.ycor():
            food()

            new_segment = Turtle("square")
            new_segment.penup()
            new_segment.color("white")
            segment.append(new_segment)





