from turtle import Turtle

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.color('white')
        self.penup()
        x=self.xcor()
        y=self.ycor()
        self.x_move=10
        self.y_move=10
        self.ball_speed=0.1

    def move(self):
        x_new=self.xcor()+self.x_move
        y_new=self.ycor()+self.y_move
        self.goto(x=x_new,y=y_new)

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1
        self.ball_speed*=0.9

    def reset_position(self):
        self.setpos(x=0,y=0)
        self.bounce_x()




