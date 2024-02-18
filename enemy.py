from turtle import Turtle, Screen, register_shape
from shoot import Shoot, Enemyshoot
from random import randint
import time
import threading
horror_alien_shape = (
    (0, 40),
    (-10, 10),
    (-20, 0),
    (-15, -5),
    (0, -30),
    (15, -5),
    (20, 0),
    (10, 10),
)
register_shape("horror_alien", horror_alien_shape)


class Enemy:
    def __init__(self):
        self.enemy_list = []

    def create(self, x, y):
        enemy = Turtle(shape="horror_alien")
        enemy.penup()
        enemy.color("green")
        enemy.goto(x, y)
        enemy.setheading(270)
        enemy.shapesize(0.5, 0.5, 1)
        self.enemy_list.append(enemy)

    def attack(self):
        while True:
            n = randint(0, len(self.enemy_list) - 1)
            shot = Enemyshoot()
            shot.createenemy()
            shot.back_on(self.enemy_list[n].xcor(), self.enemy_list[n].ycor()+20)
            time.sleep(1)




