import time
from turtle import Screen
from player import TurtlePlayer


screen = Screen()
screen.setup(width=800, height=800)
screen.bgcolor("black")
screen.title("turtle crossy road".title())
screen.tracer(0)

player = TurtlePlayer()
screen.update()

screen.listen()
screen.onkey(fun=player.move, key="Up")

game_on = True
while game_on:
    time.sleep(0.01)
    screen.update()



screen.exitonclick()