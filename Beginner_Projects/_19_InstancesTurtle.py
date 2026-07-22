import turtle
from turtle import Turtle , Screen
import random

red = turtle.Turtle()
green = turtle.Turtle()
blue = turtle.Turtle()
yellow = turtle.Turtle()

turt = [red,green,yellow,blue]
screen = Screen()
screen.setup(width=700, height=500)
screen.bgcolor("white")

red.shape("turtle")
green.shape("turtle")
yellow.shape("turtle")
blue.shape("turtle")

red.color("red")
green.color("green")
yellow.color("yellow")
blue.color("blue")

red.goto(-230,50)
green.goto(-230,-25)
yellow.goto(-230,125)
blue.goto(-230,-100)

user_bet = screen.textinput(title="Make your bet" , prompt="Which turtle will win the race? Enter a color: ")

while True:
    x = random.randint(1, 20)
    random.choice(turt).forward(x)

    if red.xcor() > 280:
        if user_bet=="red":
            turtle.write("Red Wins!", align="center", font=("Arial", 22, "bold"))
        else:
            turtle.write("Red Wins! You lose!", align="center", font=("Arial", 22, "bold"))
        break
    elif green.xcor() > 280:
        if user_bet=="green":
            turtle.write("Green Wins!", align="center", font=("Arial", 22, "bold"))
        else:
            turtle.write("Green Wins! You lose!", align="center", font=("Arial", 22, "bold"))
        break
    elif yellow.xcor() > 280:
        if user_bet=="yellow":
            turtle.write("Yellow Wins!", align="center", font=("Arial", 22, "bold"))
        else:
            turtle.write("Yellow Wins! You lose!", align="center", font=("Arial", 22, "bold"))
        break
    elif blue.xcor() > 280:
        if user_bet=="blue":
            turtle.write("Blue Wins!", align="center", font=("Arial", 22, "bold"))
        else:
            turtle.write("Blue Wins! You lose!", align="center", font=("Arial", 22, "bold"))
        break






random.choice(turt).forward(random.randint(1,20))

screen.exitonclick()



# def forward():
#     turtle.forward(10)
# def backward():
#     turtle.backward(10)
# def left():
#     turtle.left(10)
# def right():
#     turtle.right(10)
# def clear():
#     turtle.clear()
#     turtle.penup()
#     turtle.home()
#     turtle.pendown()
# screen.listen()
# screen.onkey(forward, "space")
# screen.onkey(backward, "Down")
# screen.onkey(left, "Left")
# screen.onkey(right, "Right")
# screen.onkey(clear, "c")
# screen.exitonclick()




# while True:
#     x = random.randint(1, 10)
#     y = random.choice(turt)
#     y.forward(x)






