from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, position):
        super().__init__()
        self.color("white")
        self.shape("square")
        self.penup()
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.goto(position)

    def move_up(self):
        if self.ycor() < 260:
            new_y = self.ycor() + 20
            self.setposition(self.xcor(), new_y)

    def move_down(self):
        if self.ycor() > -260:
            new_y = self.ycor() - 20
            self.setposition(self.xcor(), new_y)


