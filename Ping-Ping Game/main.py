from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import ScoreBoard
import time

#creating paddle objects
r_paddle=Paddle(350,0)
l_paddle=Paddle(-350,0)
ball=Ball()
score=ScoreBoard()


#setting up the screen
screen=Screen()
screen.setup(width=800,height=600)
screen.bgcolor('black')
screen.title('Pong')
screen.tracer(0)

#create movement keys
screen.listen()
screen.onkey(fun=r_paddle.move_up,key='Up')
screen.onkey(fun=r_paddle.move_down,key='Down')
screen.onkey(fun=l_paddle.move_up,key='w')
screen.onkey(fun=l_paddle.move_down,key='s')


game_is_on=True
while game_is_on:
    time.sleep(ball.ball_speed)
    screen.update()
    ball.move()

    #detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    #detect collison with paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    #detect when ball missed rpaddle
    if ball.xcor()>380:
        ball.reset_position()
        score.l_point()
    # detect when ball missed lpaddle
    if ball.xcor() < -380:
        ball.reset_position()
        score.r_point()


screen.exitonclick()

