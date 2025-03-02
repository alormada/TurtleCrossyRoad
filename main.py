import time
from turtle import Screen, Turtle
from player import TurtlePlayer
from traffic import Traffic
from levelboard import LevelBoard


screen = Screen()
screen.setup(width=800, height=800)
screen.bgcolor("black")
screen.title("turtle crossy road".title())
screen.tracer(0)

level = LevelBoard()
level.print_level()
traffic = Traffic(number_of_cars=10, level=level.level)
player = TurtlePlayer()
screen.update()

screen.listen()
screen.onkey(fun=player.move, key="Up")

game_on = True
while game_on:
    time.sleep(0.01)
    screen.update()

    if player.y_hitbox[1] >= 400:
        player.go_at_start()
        level.update_level()
        traffic.update_level(level.level)

    if traffic.detect_collision(player.x_hitbox, player.y_hitbox):
        game_over = LevelBoard()
        game_over.game_over()
        screen.update()
        break

    traffic.move_cars()


screen.exitonclick()