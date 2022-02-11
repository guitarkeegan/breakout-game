from turtle import Screen, Turtle
from paddle import Paddle
from blocks import Blocks
from ball import Ball
from scoreboard import Scoreboard
from cues import Cues
from time import time

screen = Screen()
screen.setup(height=800, width=1000)
screen.bgcolor("black")
screen.tracer(0)

row = Blocks()
level = 1
row.create_level(level=1)

sb = Scoreboard()


ball = Ball()

paddle = Paddle()
screen.listen()
screen.onkey(paddle.move_left, "n")
screen.onkey(paddle.move_right, ",")
screen.onkey(ball.sticky_ball, "b")

cues = Cues()
cues.controls()


on = True
while on:
    screen.update()
    ball.move()

    # paddle bounce
    if ball.ycor() <= paddle.ycor() + 15 and ball.distance(paddle) < 80 and not ball.sticky:
        ball.y_bounce()
        cues.clear()

    # freeze and move ball
    if ball.ycor() <= paddle.ycor() + 15 and ball.distance(paddle) < 80 and ball.sticky:
        cues.sticky_ball()
        ball.hideturtle()
        ball = Paddle()
        ball.stuck_ball(paddle)
        screen.onkey(ball.move_left, "n")
        screen.onkey(ball.move_right, ",")
        screen.onkey(ball.flick_ball, "v")

    # release the ball
    if ball.f_ball:
        cues.clear()
        ball.hideturtle()
        old_ball = ball
        new_ball = Ball()
        new_ball.goto(old_ball.xcor(), old_ball.ycor())
        ball = new_ball
        ball.move()
        ball.y_bounce()
        screen.onkey(paddle.move_left, "n")
        screen.onkey(paddle.move_right, ",")
        screen.onkey(ball.sticky_ball, "b")

    # back wall bounce
    if ball.ycor() >= 380:
        ball.y_bounce()

    # side bounce
    if ball.xcor() >= 480 or ball.xcor() <= -480:
        try:
            ball.x_bounce()
        except AttributeError:
            start = time()
            while time() - start < 3:
                cues.out_of_bounds()
            ball = Ball()
            paddle.goto(x=1000, y=1000)
            paddle = Paddle()
            screen.onkey(paddle.move_left, "n")
            screen.onkey(paddle.move_right, ",")
            screen.onkey(ball.sticky_ball, "b")
            cues.clear()

    # missed ball
    if ball.ycor() <= paddle.ycor() + 15 and ball.distance(paddle) > 80:
        ball.reset_game()
        sb.clear()
        sb.reset_score()
        sb.update_scoreboard()

    # destroy block
    for r in row.all_blocks:
        if ball.distance(r) < 40:
            ball.y_bounce()
            sb.clear()
            sb.add_points()
            sb.update_scoreboard()
            row.destroy_block(r)

    # level up
    if len(row.all_blocks) == 0:
        level += 1
        sb.reset_score()
        sb.level_up()
        row.all_blocks = []
        row.create_level(level)
        ball.reset_game()
        ball.current_speed *= 1.1


screen.exitonclick()
