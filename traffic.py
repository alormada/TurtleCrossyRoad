import random
from turtle import Turtle
X_RANGE = (-400, 500)
Y_RANGE = (-300, 300)
COLORS = ["red","orange","yellow","green","blue","indigo","purple"]

class Car(Turtle):
    def __init__(self, level):
        super().__init__()
        self.y_hitbox = []
        self.x_hitbox = []
        self.speed = level
        self.create_car()

    def create_car(self):
        """
        This function creates a single car
        :return:
        """
        self.shape("square")
        self.penup()
        self.shapesize(stretch_wid=2, stretch_len=5)
        self.color(random.choice(COLORS))
        self.setheading(180)
        self.goto(random.randint(X_RANGE[0], X_RANGE[1]), random.randint(Y_RANGE[0], Y_RANGE[1]))
        self.y_hitbox = [self.ycor() - 20, self.ycor() + 20]
        self.x_hitbox = [self.xcor() - 50, self.xcor() + 50]
        self.set_hitbox()

    def set_hitbox(self):
        """
        This function sets the hitbox of the car
        :return:
        """
        self.x_hitbox = [self.xcor() - 50, self.xcor() + 50]
        self.y_hitbox = [self.ycor() - 20, self.ycor() + 20]

    def go_at_start(self):
        """
        This function makes a car go at starting position
        :return:
        """
        self.goto(450, random.randint(Y_RANGE[0], Y_RANGE[1]))

    def move(self):
        """
        This function makes a car move forward
        :return:
        """
        self.forward(self.speed)
        self.set_hitbox()
