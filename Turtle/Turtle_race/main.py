from turtle import Turtle, Screen
import random

tim = Turtle()
screen = Screen()
screen.setup(width=500,height=400)
user_bet= screen.textinput(title='Make your bet',prompt='Who is going to win ?? Enter a colour ::')
colors=['red','blue','green','black','yellow']
y_positions=[-70,-90,-50,30,50]
all_turtles=[]

for turtle_index in range(0,5):
    new_turtle=Turtle(shape='turtle')
    new_turtle.penup()
    new_turtle.goto(x=-230,y=y_positions[turtle_index])
    new_turtle.color(colors[turtle_index])
    all_turtles.append(new_turtle)

is_race_on=False

if user_bet:
    is_race_on=True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor()>230:
            is_race_on=False
            winning_color=turtle.pencolor()
            if user_bet==winning_color:
                print(f'You have won. The winning color is {winning_color}')
            else:
                print(f'you lost.The winning color is {winning_color}')

        turtle.forward(random.randint(0,10))

screen.exitonclick()
