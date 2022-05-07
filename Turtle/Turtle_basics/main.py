from turtle import Turtle,Screen
import random

tim=Turtle()
tim.shape('turtle')
tim.color('red')


# for _ in range(4):
#     tim.forward(100)
#     tim.right(90)

# for _ in range(25):
#     tim.forward(7)
#     tim.penup()
#     tim.forward(7)
#     tim.pendown()

colors=['red','green','blue','brown','black','yellow','pink']
direction=[0,90,180,270]

# def different_shapes(no_of_sides):
#
#     angle=360/no_of_sides
#     for _ in range(no_of_sides):
#         tim.forward(100)
#         tim.right(angle)
#
# for sides in range(3,11):
#     tim.pencolor(random.choice(colors))
#     different_shapes(sides)

# for _ in range(1000000000):
#     tim.pen(pencolor=random.choice(colors), pensize=10)
#     tim.forward(10)
#     tim.setheading(random.choice(direction))
#     tim.speed(10)
#
# screen=Screen()
# screen.exitonclick()

def draw_spirograpgh(size_of_spirograph):
    for _ in range(int(360/size_of_spirograph)):
        tim.pen(pencolor=random.choice(colors))
        tim.speed('fastest')
        tim.circle(40)
        tim.setheading(tim.heading()+size_of_spirograph)

draw_spirograpgh(2)

