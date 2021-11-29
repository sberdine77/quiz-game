class RankingModel():
	def __init__(self, name, points: int = None):
		self.name = name or "---"
		self.points = points or 0
	
	def asDictionary(self):
		dict = {"name": self.name, "points": self.points}
		return dict