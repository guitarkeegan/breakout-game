from turtle import Turtle, Screen


class Paddle(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("square")
        self.turtlesize(stretch_wid=8.0, stretch_len=1.0)
        self.goto(x=0, y=-350)
        self.setheading(90)
        self.color("white")
        self.f_ball = False

    def move_left(self):
        left = self.xcor() - 20
        self.setx(left)

    def move_right(self):
        right = self.xcor() + 20
        self.setx(right)

    def stuck_ball(self, paddle):
        self.shape("circle")
        self.color("#ff33cc")
        self.turtlesize(stretch_len=1, stretch_wid=1)
        self.goto(paddle.xcor(), paddle.ycor() + 25)

    def move(self):
        pass

    def flick_ball(self):
        self.f_ball = True




