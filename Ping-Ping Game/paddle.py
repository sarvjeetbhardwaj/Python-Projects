from turtle import Turtle

class Paddle(Turtle):

    def __init__(self,x,y):
        super().__init__()
        self.x=x
        self.y=y
        self.shape('square')
        self.shapesize(stretch_wid=5,stretch_len=1)
        self.color('white')
        self.penup()
        self.goto(self.x, self.y)

    def move_up(self):
        new_y=self.ycor()+20
        self.goto(x=self.xcor(),y=new_y)

    def move_down(self):
        new_y=self.ycor()-20
        self.goto(x=self.xcor(),y=new_y)



