import turtle
import random


screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Turtle ile Mandala Deseni")


mandala = turtle.Turtle()
mandala.speed(0)
colors = ["red", "purple", "blue", "green", "yellow", "orange", "pink", "cyan"]


def draw_mandala():
    for i in range(36):
        mandala.pencolor(random.choice(colors))
        mandala.circle(100)
        mandala.right(10)
        for j in range(6):
            mandala.pencolor(random.choice(colors))
            mandala.circle(50)
            mandala.right(60)


draw_mandala()


screen.exitonclick()
