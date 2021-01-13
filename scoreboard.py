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
        self.goto(15, 250)
        self.clear()
        self.write(f"Player1 {self.left_score}  {self.right_score}  Player2", align="center", font=("Courier", 40, "normal"))

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

    def player1_wins(self):
        self.goto(0,0)
        self.write("Player 1 wins", align="center", font=("Courier", 25, "normal"))

    def player2_wins(self):
        self.goto(0,0)
        self.write("Player 1 wins", align="center", font=("Courier", 25, "normal"))




