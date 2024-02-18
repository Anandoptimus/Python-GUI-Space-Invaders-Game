from turtle import Turtle, register_shape
from shoot import Shoot

register_shape("alien_spaceship", ((0, -50), (-20, 30), (-40, -20), (0, 20), (40, -20), (20, 30)))
Turtle(shape="alien_spaceship", visible=True)
Turtle(shape="short_line", visible=True)


class Hero(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("alien_spaceship")
        self.color("green")
        self.penup()
        self.goto(0, -230)
        self.setheading(270)
        self.shapesize(0.5, 0.5, 1)
        self.xcorr = 10
        self.ycorr = 10

    def go_right(self):
        new_x = self.xcor() + 20
        self.goto((new_x, self.ycor()))

    def go_left(self):
        new_x = self.xcor() - 20
        self.goto((new_x, self.ycor()))

    def shoot(self):
        if not Shoot.in_motion:
            shot = Shoot()
            shot.create()
            shot.move_on(xcor=self.xcor(), ycor=self.ycor() + 20)




