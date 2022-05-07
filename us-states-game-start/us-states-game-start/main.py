import turtle
from turtle import Screen
import pandas as pd

screen=Screen()
screen.title('US States Game')
img_file= 'blank_states_img.gif'
screen.addshape(img_file)
turtle.shape(img_file)

df=pd.read_csv('50_states.csv')

no_of_chances=0
game_is_on=True

while game_is_on:

    if no_of_chances == 50:
        turtle.write('Game over')
        game_is_on = False

    answer = screen.textinput(title=f'{no_of_chances}/50 States Game', prompt='whats another state name ??')

    if answer.title()=='Exit':
        break

    if answer.title() in list(df['state']):
        t=turtle.Turtle()
        t.penup()
        t.hideturtle()
        t.goto(x=int(df[df['state']==answer.title()]['x']),y=int(df[df['state']==answer.title()]['y']))
        t.write(answer)
        no_of_chances = no_of_chances + 1

    elif answer.title() not in list(df['state']):
        no_of_chances = no_of_chances + 1
