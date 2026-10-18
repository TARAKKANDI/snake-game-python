from turtle import Screen, Terminator
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

WALL = 280  # head beyond this on x or y means it hit the wall


def main():
    screen = Screen()
    screen.setup(width=600, height=600)
    screen.bgcolor("black")
    screen.title("My Snake Game")
    screen.tracer(0)

    snake = Snake()
    food = Food()
    scoreboard = Scoreboard()

    screen.listen()
    screen.onkey(snake.up, "Up")
    screen.onkey(snake.down, "Down")
    screen.onkey(snake.left, "Left")
    screen.onkey(snake.right, "Right")

    game_is_on = True
    while game_is_on:
        screen.update()
        time.sleep(0.1)
        snake.move()

        # Detect collision with food
        if snake.head.distance(food) < 15:
            food.refresh(snake.segments)
            snake.extend()
            scoreboard.increase_score()

        # Detect collision with wall
        if (snake.head.xcor() > WALL or snake.head.xcor() < -WALL
                or snake.head.ycor() > WALL or snake.head.ycor() < -WALL):
            game_is_on = False
            scoreboard.game_over()

        # Detect collision with tail
        for segment in snake.segments[1:]:
            if snake.head.distance(segment) < 10:
                game_is_on = False
                scoreboard.game_over()
                break

    screen.update()
    screen.exitonclick()


if __name__ == "__main__":
    try:
        main()
    except Terminator:
        # Window was closed while the game was running - exit quietly
        pass