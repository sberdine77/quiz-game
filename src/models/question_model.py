from enum import Enum

class QuestionModel():
	def __init__(self, id=None, title=None, level=None):
		self.id = id or -1
		self.title = title or ""
		if level == "easy":
			self.level = QuestionLevel.EASY
		elif level == "medium":
			self.level = QuestionLevel.MEDIUM
		elif level == "hard":
			self.level = QuestionLevel.HARD
		else:
			self.level = QuestionLevel.MEDIUM

class QuestionLevel(Enum):
	EASY = 1
	MEDIUM = 2
	HARD = 3