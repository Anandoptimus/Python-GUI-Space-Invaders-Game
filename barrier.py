from turtle import Turtle
import random


class Barrier:
    def __init__(self):
        self.new_brick = []

    def create(self, x, y):
        # color = random.choice(COLORS)
        new_brick = Turtle(shape='square')
        new_brick.penup()
        new_brick.color("green")
        new_brick.shapesize(0.5, 0.5, 1)
        new_brick.goto(x, y)
        new_brick.setheading(90)
        new_brick.speed(0)
        self.new_brick.append(new_brick)
    # for i in range(5):
        #
        #     ycorr -= 100







