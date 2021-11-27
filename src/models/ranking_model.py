class RankingModel():
	def __init__(self, name, points=None):
		self.name = name or "---"
		self.points = points or 0
	