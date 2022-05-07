import colorgram
import turtle as turtle_module
import random
from turtle import Screen

turtle_module.colormode(255)
print(turtle_module.screensize())
tim=turtle_module.Turtle()

colors = colorgram.extract('image.jpg', 30)

rgb_colors = []
for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    new_color = (r, g, b)
    rgb_colors.append(new_color)

tim.penup()
tim.setpos(-300,-250)

for y in range(20):
    for _ in range(20):
        tim.pendown()
        tim.dot(20,random.choice(rgb_colors))
        tim.penup()
        tim.forward(30)
        tim.pendown()
        tim.dot(20,random.choice(rgb_colors))
    tim.penup()
    tim.setpos(-300,tim.ycor()+25)











screen=Screen()
screen.exitonclick()




