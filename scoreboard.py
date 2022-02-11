from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.points = 0
        self.penup()
        self.hideturtle()
        self.pencolor("white")
        self.goto(x=250, y=300)
        self.level = 1
        self.update_scoreboard()


    def add_points(self):
        self.points += 10

    def update_scoreboard(self):
        self.write(f"Level {self.level} Score: {self.points}", font=("Courier", 20, "normal"))

    def reset_score(self):
        self.points = 0

    def level_up(self):
        self.level += 1




