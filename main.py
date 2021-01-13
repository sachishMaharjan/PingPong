from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time


screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Ping Pong game")
screen.tracer(0)

r_paddle = Paddle((370, 0))
l_paddle = Paddle((-380, 0))

screen.listen()
# Control for right paddle
screen.onkey(r_paddle.move_up, "Up")
screen.onkey(r_paddle.move_down, "Down")

# Control for left paddle
screen.onkey(l_paddle.move_up, "w")
screen.onkey(l_paddle.move_down, "s")

ball = Ball()
scoreboard = Scoreboard()


game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    ball.move()
    scoreboard.middle_line()
    screen.update()

    # Detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -270:
        ball.bounce_wall()

    # Detect collision with paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 340 or ball.distance(l_paddle) < 50 and ball.xcor() < -340:
        ball.bounce_paddle()

    # Update score
    # Detect R paddle misses
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.increase_left_player_score()

    # Detect L paddle misses
    if ball.xcor() < -390:
        ball.reset_position()
        scoreboard.increase_right_player_score()

    # Detect when either player score is 10:
    if scoreboard.left_score == 10:
        game_is_on = False
        scoreboard.player1_wins()
    elif scoreboard.right_score == 10:
        game_is_on = False
        scoreboard.player2_wins()


screen.exitonclick()


