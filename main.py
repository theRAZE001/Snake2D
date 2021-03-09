from turtle import Screen
from snake import Snake
from food import Food
from scoreBoard import ScoreBoard
import time
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")


segments = []
screen.tracer(0)

snake = Snake()
food = Food()
scoreBoard = ScoreBoard()

screen.listen()
screen.onkeypress(snake.up, "Up")
screen.onkeypress(snake.down, "Down")
screen.onkeypress(snake.left, "Left")
screen.onkeypress(snake.right, "Right")


game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)

    snake.move()
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreBoard.increase_score()

    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        scoreBoard.reset()
        snake.reset()

    for segment in snake.segments[1:-1]:
        if snake.head.distance(segment) < 10:
            scoreBoard.reset()
            snake.reset()



screen.exitonclick()
