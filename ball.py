from turtle import Turtle

# Constants
Y_DISTANCE = 10
X_DISTANCE = 10


class Ball(Turtle):

	def __init__(self):
		"""Constructor for Paddle"""
		super().__init__()
		self.shape("circle")
		self.color("white")
		self.penup()
		self.goto(0, 0)

		self.x_move = X_DISTANCE
		self.y_move = Y_DISTANCE

	def move(self):
		"""Movement of Ball"""
		new_x = self.xcor() + self.x_move
		new_y = self.ycor() + self.y_move
		self.goto(new_x, new_y)

	def bounce_top(self):
		"""This function bounces the ball when it touches the top wall"""

		self.y_move *= -1

	def bounce_side(self):
		"""This function bounces the ball when it touches the paddle"""

		self.x_move *= -1

	def ball_reset(self):
		"""This function bounces the ball when it touches the paddle"""

		self.goto(0, 0)
		self.bounce_side()
