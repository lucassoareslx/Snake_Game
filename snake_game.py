from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time


screen = Screen()
screen.setup(width=800,height=800)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
score = Scoreboard()

screen.listen()
screen.onkeypress(snake.up,"Up")
screen.onkeypress(snake.down,"Down")
screen.onkeypress(snake.left,"Left")
screen.onkeypress(snake.right,"Right")

game_in_on = True

while game_in_on:
    screen.update()
    time.sleep(0.05)
    snake.move()

    if snake.head.distance(food) < 15:
        score.scorepoint()
        snake.extend()
        food.refresh()
    
    if snake.head.xcor() > 395 or snake.head.xcor() < -395 or snake.head.ycor() > 395 or snake.head.ycor() < -395:
        score.game_over()
        game_in_on = False
    
    for segment in snake.segments:
        if segment == snake.head:
            pass
        elif snake.head.distance(segment) < 10:
            game_in_on = False
            score.game_over()

    

screen.exitonclick()