from pathlib import Path
import random
import turtle

try:
    import colorgram as gc
except ImportError:
    gc = None


def load_palette(image_name="image.png", number_of_colors=30):
    image_path = Path(__file__).with_name(image_name)
    if gc is None or not image_path.exists():
        return [
            (239, 245, 240), (236, 239, 245), (229, 219, 109), (230, 237, 231),
            (216, 165, 102), (219, 75, 54), (59, 108, 163), (130, 29, 38),
            (140, 81, 54), (47, 151, 112), (183, 140, 173), (71, 41, 32),
        ]

    colors = gc.extract(str(image_path), number_of_colors)
    return [(color.rgb.r, color.rgb.g, color.rgb.b) for color in colors]


def random_color(palette):
    return random.choice(palette)


palette = load_palette()

screen = turtle.Screen()
screen.colormode(255)

artist = turtle.Turtle()
artist.hideturtle()
artist.penup()
artist.speed("fastest")

start_x = -300
start_y = -300
dot_spacing = 50
dot_size = 20
grid_size = 10

for row in range(grid_size):
    for col in range(grid_size):
        artist.goto(start_x + col * dot_spacing, start_y + row * dot_spacing)
        artist.dot(dot_size, random_color(palette))

screen.exitonclick()


