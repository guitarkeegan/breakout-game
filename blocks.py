import random
from turtle import Turtle, Screen


class Blocks(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("square")
        self.turtlesize(stretch_len=3, stretch_wid=1)
        self.goto(x=-450, y=0)
        self.row_num = {1: 0, 2: 25, 3: 50, 4: 75, 5: 100, 6: 125, 7: 150, 8: 175, 9: 200, 10: 225}
        self.row_colors = {1: "#FF0000", 2: "#FF3EC0", 3: "#00FF00", 4: "#FFFF33", 5: "#FF8000",
                           6: "#00FFFF", 7: "#CC0000", 8: "#0000CC", 9: "#990099", 10: "#CCFFFF"}
        self.all_blocks = []

    def create_row(self, row):
        last_block_x = [-550]
        for block in range(10):
            block = Blocks()
            block.penup()
            block.color(self.row_colors[row])
            block.sety(self.row_num[row])
            block.setx(last_block_x[-1] + 99)
            last_block_x.append(block.xcor())
            self.all_blocks.append(block)

    def destroy_block(self, block):
        self.all_blocks.pop(self.all_blocks.index(block))
        block.color("black")
        block.speed("fastest")
        block.goto(x=1000, y=1000)

    def create_level(self, level):
        for row in range(level):
            rand_row = random.randint(1, 10)
            self.create_row(rand_row)







