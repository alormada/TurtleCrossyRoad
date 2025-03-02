import time
from turtle import Screen, Turtle
from player import TurtlePlayer
from traffic import Car


screen = Screen()
screen.setup(width=800, height=800)
screen.bgcolor("black")
screen.title("turtle crossy road".title())
screen.tracer(0)

cars = []
level = 1
for i in range(10):
    cars.append(Car(level))
player = TurtlePlayer()
# mark = Turtle()
# mark.shape("circle")
# mark.color("red")
# mark.shapesize(0.2)
# mark.penup()
# mark.goto(0, player.ycor() - 15)
screen.update()

screen.listen()
screen.onkey(fun=player.move, key="Up")

game_on = True
while game_on:
    time.sleep(0.01)
    screen.update()

    if player.y_hitbox[1] >= 400:
        player.go_at_start()
        player.set_hitbox()
        level += 1
        for car in cars:
            car.speed += 1
        cars.append(Car(level))
        cars[-1].go_at_start()


    # print("\n==============================================\n")
    for car in cars:
        # print()
        # print(f"T: {player.x_hitbox} C: {car.x_hitbox}")
        # print(f"T: {player.y_hitbox} C: {car.y_hitbox}")
        if car.x_hitbox[1] >= player.x_hitbox[1] >= car.x_hitbox[0] and (
                car.y_hitbox[0] <= player.y_hitbox[0] <= car.y_hitbox[1] or car.y_hitbox[0] <= player.y_hitbox[1] + 5 <=
                car.y_hitbox[1]):
            game_on = False
            screen.update()
            break
    for car in cars:
        car.move()
        if car.xcor() + 50 < -400:
            car.go_at_start()



screen.exitonclick()