from turtle import Turtle


class Cues(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.pencolor("red")
        self.goto(x=-250, y=300)
        self.level = 1

    def out_of_bounds(self):
        self.write("Lose your ball? Wait one moment...", font=("Courier", 20, "normal"))

    def sticky_ball(self):
        self.write("Ball is sticky!! Press 'v' to release.", font=("Courier", 20, "normal"))

    def controls(self):
        self.write("Press 'b' to catch the ball.", font=("Courier", 20, "normal"))


