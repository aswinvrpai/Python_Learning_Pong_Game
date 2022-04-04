from turtle import Turtle

# Constants
Y_UP_DISTANCE = 20
Y_DOWN_DISTANCE = 20
Y_TOP_END = 270
Y_BOTTOM_END = -270


class Paddle(Turtle):

	def __init__(self, position):
		"""Constructor for Paddle"""
		super().__init__()
		self.shape("square")
		self.color("white")
		self.shapesize(stretch_len=1, stretch_wid=5)
		self.penup()
		self.goto(position)

	def paddle_up(self):
		"""Move the paddle up by 20 units"""

		new_y = self.ycor() + Y_UP_DISTANCE

		# Move the paddle only till the bottom of screen;
		if new_y < Y_TOP_END:
			self.goto(self.xcor(), new_y)

	def paddle_down(self):
		"""Move the paddle down by 20 units"""

		new_y = self.ycor() - Y_DOWN_DISTANCE

		# Move the paddle only till the bottom of screen;
		if new_y > Y_BOTTOM_END:
			self.goto(self.xcor(), new_y)

