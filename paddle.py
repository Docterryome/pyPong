from turtle import Turtle

SQUARE_SIZE = 20
WIDTH = 20 / SQUARE_SIZE
HEIGHT = 100 / SQUARE_SIZE
MOVE_SPEED = 50


class Paddle(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("square")
        self.shapesize(stretch_wid=HEIGHT, stretch_len=WIDTH)
        self.color("white")

    def move_up(self):
        move_to = self.ycor() + MOVE_SPEED
        self.sety(move_to)

    def move_down(self):
        move_to = self.ycor() - MOVE_SPEED
        self.sety(move_to)