from turtle import Screen
from player import Player
from cars import Cars
import time

#setting up player
player=Player()
car=Cars()

#setting up the screen
screen=Screen()
screen.setup(width=600,height=600)
screen.tracer(0)

#create movement
screen.listen()
screen.onkey(fun=player.move_up,key='Up')
screen.onkey(fun=player.move_down,key='Down')

game_is_on=True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car.create_car()
    car.move_cars()

   #detect collision with the turtle
    for cars in car.all_cars:
        if cars.distance(player) < 20:
            game_is_on=False

    #detect successful crossing
    if player.isatfinishline():
        player.go_to_start_line()
        car.car_speed()


screen.exitonclick()


