import time
from turtle import Screen
from paddle import Paddle
from ball import Ball
from score import ScoreBoard

# Constants;
BACKGROUND_COLOR = "black"
GAME_TITLE = "PONG GAME 2022"
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# New Screen;
screen = Screen()
screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
screen.bgcolor(BACKGROUND_COLOR)
screen.title(GAME_TITLE)
screen.tracer(0)

# Left Paddle;
left_paddle = Paddle((-350, 0))

# Right Paddle;
right_paddle = Paddle((350, 0))

# Ball;
ball = Ball()

# Scoreboard;
scoreboard = ScoreBoard()

# Listening Events to Keys in keyboard
screen.listen()
screen.onkey(left_paddle.paddle_up, "w")
screen.onkey(right_paddle.paddle_up, "Up")
screen.onkey(left_paddle.paddle_down, "s")
screen.onkey(right_paddle.paddle_down, "Down")


game_on = True
while game_on:
	time.sleep(0.1)
	screen.update()

	# Move the ball
	ball.move()

	# Detect Ball collision with Top wall;
	if ball.ycor() > 280 or ball.ycor() < -280:
		ball.bounce_top()

	# Detect Ball collision with Left Paddle;
	if ball.distance(left_paddle) < 50 and ball.xcor() < -320:
		ball.bounce_side()

	# Detect Ball collision with Right Paddle;
	if ball.distance(right_paddle) < 50 and ball.xcor() < 320:
		ball.bounce_side()

	# If Ball goes out of bound at Right Paddle;
	if ball.xcor() > 380:
		scoreboard.l_point()
		ball.ball_reset()

	# If Ball goes out of bound at Left Paddle;
	if ball.xcor() < -380:
		scoreboard.r_point()
		ball.ball_reset()

# Exit on click;
screen.exitonclick()
