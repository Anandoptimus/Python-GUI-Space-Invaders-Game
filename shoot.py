from turtle import Turtle, register_shape
import time

register_shape("short_line", ((0, 5), (0, -5), (0.1, -10), (0.1, 0)))
Turtle(shape="short_line", visible=True)
register_shape("line", ((0, 5), (0, -8), (0.1, -12), (0.1, 0)))
Turtle(shape="line", visible=True)


class Shoot(Turtle):
    in_motion = False
    out_motion = True

    def __init__(self):
        super().__init__()
        self.list = []

    def create(self):
        shoot = Turtle(shape='short_line')
        shoot.penup()
        shoot.color("green")
        shoot.setheading(90)
        # shoot.goto(x, y)
        self.list.append(shoot)

    def move_on(self, xcor, ycor):
        if not Shoot.in_motion:
            Shoot.in_motion = True
            for i in self.list:
                # i.goto(xcor, ycor)
                for _ in range(40):
                    i.forward(10)
                    time.sleep(0.08)
            Shoot.in_motion = False

    # def back_on(self):
    #     if Shoot.out_motion:
    #         Shoot.out_motion = False
    #         self.goto(self.xcor, self.ycor)
    #         for _ in range(50):
    #             self.backward(10)
    #             time.sleep(0.08)
    #         Shoot.out_motion = True


class Enemyshoot(Turtle):
    out_motion = True

    def __init__(self):
        super().__init__()
        self.enemylist = []

    def createenemy(self):
        shoot = Turtle(shape='line')
        shoot.penup()
        shoot.color("green")
        shoot.setheading(90)
        # self.goto(x, y)
        self.enemylist.append(shoot)

    def back_on(self, x, y):
        for i in self.enemylist:
            for _ in range(50):
                i.goto(x, y)
                i.backward(10)
                time.sleep(0.08)
