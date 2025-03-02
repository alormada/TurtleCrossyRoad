from turtle import Turtle

class TurtlePlayer(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.shape("turtle")
        self.shapesize(1.5)
        self.goto(0, -380)
        self.setheading(90)
        self.y_hitbox = [self.ycor() - 15, self.ycor() + 25]
        self.x_hitbox = [self.xcor() - 15, self.xcor() + 15]
        self.set_hitbox()

    def move(self):
        """
        This function makes turtle move
        :return:
        """
        self.forward(20)
        self.set_hitbox()

    def go_at_start(self):
        self.goto(0, -380)
        self.set_hitbox()

    def set_hitbox(self):
        """
        This function sets hitbox parameters of the turtle
        :return:
        """
        self.y_hitbox = [self.ycor() - 15, self.ycor() + 25]


