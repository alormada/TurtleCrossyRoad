from turtle import Turtle
FONT = ("Arial", 20, "normal")

class LevelBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.level = 1
        self.goto(-380, 350)

    def print_level(self):
        self.write(arg=f"Level: {self.level}", align="left", font=FONT)

    def update_level(self):
        self.level += 1
        self.clear()
        self.print_level()

    def game_over(self):
        self.goto(0, 0)
        self.write(arg=f"game over".upper(), align="center", font=FONT)