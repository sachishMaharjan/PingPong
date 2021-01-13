from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.left_score = 0
        self.right_score = 0
        self.goto(0, 200)
        self.update_score()

    def increase_left_player_score(self):
        self.left_score += 1
        self.update_score()

    def increase_right_player_score(self):
        self.right_score += 1
        self.update_score()

    def update_score(self):
        self.goto(0, 200)
        self.clear()
        self.write(f"{self.left_score}  {self.right_score}", align="center", font=("Courier", 80, "normal"))

    def middle_line(self):
        self.speed("fastest")
        self.goto(0, 300)
        self.pensize(5)
        self.setheading(270)
        for _ in range(15):
            self.pendown()
            self.forward(20)
            self.penup()
            self.forward(20)

    def game_over(self):
        self.write("Game Over.", align="center", font=("Courier", 25, "normal"))




