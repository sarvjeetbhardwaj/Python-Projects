from turtle import  Screen
import time
from snake import Snake
from food import Food
from scoreboard import ScoreBoard


screen=Screen()
screen.setup(width=600,height=600)
screen.bgcolor('black')
screen.title('My Snake game')
screen.tracer(0)

snake=Snake()
food=Food()
scoreboard=ScoreBoard()

screen.listen()
screen.onkey(fun=snake.right,key='Right')
screen.onkey(fun=snake.left,key='Left')
screen.onkey(fun=snake.up,key='Up')
screen.onkey(fun=snake.down,key='Down')


game_is_on=True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    #Detect colliion with food
    if snake.head.distance(food) < 15:
        food.refresh()
        scoreboard.increase_score()
    #Detect collison with wall
    if snake.head.xcor()>280 or snake.head.xcor()<-280 or snake.head.ycor()>280 or snake.head.xcor()<-280:
        scoreboard.game_over()
        game_is_on = False

screen.exitonclick()