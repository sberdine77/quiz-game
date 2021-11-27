class AlternativeModel():
	def __init__(self, id=None, questionId=None, title=None, isCorrect=None):
		self.id = id or -1
		self.questionId = questionId or -1
		self.title = title or ""
		if isCorrect == "TRUE":
			self.isCorrect = True
		else:
			self.isCorrect = False
