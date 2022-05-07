from turtle import Turtle
START_POSITION=(0, -280)

class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.go_to_start_line()
        self.setheading(90)
        self.shape('turtle')

    def move_up(self):
        self.forward(10)

    def move_down(self):
        self.back(10)

    def go_to_start_line(self):
        self.goto(START_POSITION)

    def isatfinishline(self):
        if self.ycor()>280:
            return True
        else:
            return False

