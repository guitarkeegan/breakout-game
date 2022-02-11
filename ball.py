from turtle import Turtle
import random

STARTING_X = [-1, -2, 1, 2]

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.goto(x=0, y=-20)
        self.setheading(270)
        self.current_speed = 4
        self.speed(self.current_speed)
        self.move_x = random.choice(STARTING_X)
        self.move_y = -3
        self.sticky = False
        self.f_ball = False

    def move(self):
        new_x = self.xcor() + self.move_x
        new_y = self.ycor() + self.move_y
        self.goto(new_x, new_y)

    def y_bounce(self):
        self.move_y = self.move_y * -1

    def x_bounce(self):
        self.move_x = self.move_x * -1

    def reset_game(self):
        self.color("black")
        self.goto(x=0, y=-20)
        self.color("white")
        self.move_x = random.choice(STARTING_X)
        self.move()

    def sticky_ball(self):
        self.sticky = True

    def from_sticky(self):
        self.goto()




