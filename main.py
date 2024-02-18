from turtle import Screen
from hero import Hero
from enemy import Enemy
from barrier import Barrier
from shoot import Shoot, Enemyshoot

screen = Screen()
hero = Hero()
enemy = Enemy()
barrier = Barrier()
shoot = Shoot()
enemyShoot = Shoot()

count = 50
value = 350
x = value - count
for i in range(12):
    x -= 50
    enemy.create(x=x, y=200)

x_cor = value-count
for j in range(31):
    x_cor -= 20
    if j % 2 == 0:
        barrier.create(x=x_cor, y=120)
        barrier.create(x=x_cor, y=80)
    else:
        barrier.create(x=x_cor, y=100)


screen.listen()
screen.setup(700, 500)
screen.title("Space Invaders")
screen.bgcolor("black")
screen.onkey(hero.go_right, "Right")
screen.onkey(hero.go_left, "Left")
screen.onkey(hero.shoot, "space")
enemy.attack()
# screen.tracer(0)
#
# while True:
#     screen.update()
#







screen.exitonclick()
