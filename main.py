import random
from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from time import sleep
from scoreboard import Scoreboard


def middle_line(height):
    num_of_squares = int(height / 40)
    start_pos = height / 2
    t = Turtle()
    t.penup()
    t.sety(start_pos)
    t.pensize(10)
    t.pencolor("white")
    t.hideturtle()
    t.setheading(270)
    for x in range(num_of_squares):
        t.pendown()
        t.forward(25)
        t.penup()
        t.forward(40)


speed_delta = 2
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor('black')
screen.title("Pong")
screen.tracer(0)

height = (screen.window_height() / 2) - 20
width = (screen.window_width() / 2) - 20

paddle1 = Paddle()
paddle2 = Paddle()
middle_line(screen.window_height())
scoreboard = Scoreboard()
ball = Ball()


paddle1.setx(380)
paddle2.setx(-390)


screen.listen()

screen.onkeypress(fun=paddle1.move_up, key="Up")
screen.onkeypress(fun=paddle2.move_up, key="w")
screen.onkeypress(fun=paddle1.move_down, key="Down")
screen.onkeypress(fun=paddle2.move_down, key="s")

screen.update()


while True:
    sleep(0.001)
    if width - 15 < ball.xcor() and ball.x_direction == 1:
        if abs(paddle1.ycor() - ball.ycor()) < 50:
            ball.update_x()
            ball.update_ball_speed()
        else:
            scoreboard.update_lscore()
            ball.reset()
    elif ball.xcor() < (width * -1) + 8 and ball.x_direction == -1:
        if abs(paddle2.ycor() - ball.ycor()) < 50:
            ball.update_x()
            ball.update_ball_speed()
        else:
            scoreboard.update_rscore()
            ball.reset()
    if height + 10 < ball.ycor() or ball.ycor() < (height * -1):
        ball.update_y()

    ball.move()
    screen.update()

screen.exitonclick()

