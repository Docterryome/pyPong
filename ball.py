from turtle import Turtle
import random


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.y_speed = random.randint(1, 4)
        self.penup()
        self.shape("circle")
        self.color("white")
        self.ball_speed = 1
        self.x_direction = random.choice([1, -1])
        self.y_direction = random.choice([1, -1])

    def move(self):
        dx = self.xcor() + (self.ball_speed * self.x_direction)
        dy = self.ycor() + (self.y_speed * self.y_direction)
        self.setx(dx)
        self.sety(dy)

    def change_y(self):
        self.y_speed = random.randint(1, 7)

    def update_x(self):
        self.x_direction = self.x_direction * -1
        self.change_y()
        print(self.ball_speed)

    def update_y(self):
        self.y_direction = self.y_direction * -1

    def update_ball_speed(self):
        self.ball_speed += 1

    def reset(self):
        super().reset()
        self.__init__()
