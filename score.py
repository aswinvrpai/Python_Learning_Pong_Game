from turtle import Turtle

# Constants
ALIGNMENT = "center"
FONT = ("Arial", 8, "normal")


class ScoreBoard(Turtle):

	def __init__(self):
		"""Constructor for Scoreboard class"""

		super().__init__()

		# Create a header at the top of screen;
		self.score = 0
		self.penup()
		self.color("white")
		self.hideturtle()
		self.lscore = 0
		self.rscore = 0

		# Write the header for turtle object(score)
		self.score_update()

	def score_update(self):
		"""Writes out the score on the screen"""
		self.clear()
		self.goto(-100, 200)
		self.write(self.lscore, move=False, align=ALIGNMENT, font=("Courier", 80, "normal"))

		self.goto(100, 200)
		self.write(self.rscore, move=False, align=ALIGNMENT, font=("Courier", 80, "normal"))

	def score_gameover(self):
		"""Writes out the GAME OVER statement on the screen"""

		self.goto(0, 0)
		self.color("white")
		self.write(f"GAME OVER", move=False, align=ALIGNMENT, font=FONT)

	def l_point(self):
		"""Function which increases the point by 1"""

		self.lscore += 1
		self.clear()
		self.score_update()

	def r_point(self):
		"""Function which increases the point by 1"""

		self.rscore += 1
		self.clear()
		self.score_update()

