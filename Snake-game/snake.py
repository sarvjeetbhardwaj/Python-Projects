
from turtle import Turtle

X_POS=[0,-25,-50]
MOVE_DISTANCE=20
UP=90
DOWN=270
LEFT=180
RIGHT=0

class Snake:
    def __init__(self):
        self.snake=[]
        self.create_snake()
        self.head=self.snake[0]

    def create_snake(self):
        for turtles in range(0, 3):
            tim = Turtle(shape='square')
            tim.penup()
            tim.setpos(x=X_POS[turtles], y=0)
            tim.color('white')
            self.snake.append(tim)

    def move(self):
        for seg_num in range(len(self.snake) - 1, 0, -1):
            x_new = self.snake[seg_num - 1].xcor()
            y_new = self.snake[seg_num - 1].ycor()
            self.snake[seg_num].goto(x=x_new, y=y_new)
        self.snake[0].forward(MOVE_DISTANCE)

    def up(self):
        for segment in self.snake:
            if segment.heading() !=DOWN:
                 return segment.setheading(UP)

    def down(self):
        for segment in self.snake:
            if segment.heading() != UP:
                return segment.setheading(DOWN)

    def left(self):
        for segment in self.snake:
            if segment.heading() != RIGHT:
                return segment.setheading(LEFT)

    def right(self):
        for segment in self.snake:
            if segment.heading() != LEFT:
                return segment.setheading(RIGHT)





