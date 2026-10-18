from turtle import Turtle
import random


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("red")
        self.speed("fastest")
        self.refresh()

    def refresh(self, snake_segments=()):
        # Snap to the 20px grid so the snake can line up with the food,
        # and never spawn the food on top of the snake.
        while True:
            random_x = random.randrange(-280, 281, 20)
            random_y = random.randrange(-280, 281, 20)
            if all(seg.distance(random_x, random_y) > 15 for seg in snake_segments):
                break
        self.goto(random_x, random_y)