from turtle import Turtle

class TurtlePlayer(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.shape("turtle")
        self.goto(0, -380)
        self.setheading(90)

    def move(self):
        self.forward(20)


