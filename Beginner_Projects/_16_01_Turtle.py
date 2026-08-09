from turtle import Turtle , Screen

colors = [
    "black",
    "white",
    "gray",
    "red",
    "orange",
    "yellow",
    "green",
    "blue",
    "purple",
    "pink",
    "brown",
    "cyan",
    "magenta",
    "gold",
    "silver",
    "violet",
    "indigo",
    "turquoise",
    "beige",
    "maroon",
    "olive",
    "navy",
    "teal",
    "lime",
    "coral",
    "salmon",
    "khaki",
    "tan",
    "plum",
    "orchid",
    "chocolate",
    "crimson",
    "aqua",
    "lavender",
    "ivory",
    "wheat",
    "sienna",
    "tomato",
    "magenta"
]

x = Turtle()
x.shape("turtle")
x.color("coral")


screen = Screen()

def loop(o):
    x.forward(10*o)
    x.color(colors[o])
    x.right(90)
    x.color(colors[o+1])
    x.forward(10*o)
    x.color(colors[o+2])
    x.right(90)
    x.color(colors[o+3])

for i in range(1 , 100):
    loop(i)
    if i == 13:
        break
    # screen.exitonclick()
