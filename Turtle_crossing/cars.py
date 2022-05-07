from turtle import Turtle
import random

COLORS=['red','green','orange','blue','yellow','purple']
STARTING_MOVE_DISTANCE=5
INCREMENT_DISTANCE=10

class Cars:

    def __init__(self) :
        self.all_cars=[]
        self.carspeed=STARTING_MOVE_DISTANCE


    def create_car(self):
        random_choice=random.randint(1,6)
        if random_choice==1:
            new_car=Turtle(shape='square')
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.penup()
            new_car.color(random.choice(COLORS))
            new_y=random.randint(-250,250)
            new_car.goto(x=300,y=new_y)
            self.all_cars.append(new_car)

    def move_cars(self):
        for car in self.all_cars:
            car.backward(STARTING_MOVE_DISTANCE)

    def car_speed(self):
        self.carspeed+=INCREMENT_DISTANCE








