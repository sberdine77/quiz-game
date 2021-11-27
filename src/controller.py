from _typeshed import Self
import csv
from typing import List
from models.question_model import QuestionModel, QuestionLevel
from models.alternative_model import AlternativeModel
from models.ranking_model import RankingModel

__POINTS_FOR_EASY_QUESTION = 10
__POINTS_FOR_MEDIUM_QUESTION = 20
__POINTS_FOR_HARD_QUESTION = 30

class Controller():
	def __init__(self):
		self.__questionsList
		self.__currentQuestionAlternativesList
		self.__player
		self.__readQuestions()

	def getQuestionsList(self) -> List[QuestionModel]:
		return self.__questionsList
	
	def getcurrentQuestionAlternativesList(self, questionId) -> List[AlternativeModel]:
		self.__readQuestionAlternativesList(questionId=questionId)
		return self.__currentQuestionAlternativesList
	
	def setPlayer(self, name):
		self.__player = RankingModel(name=name)
	
	def addPointsForQuestion(self, questionLevel: QuestionLevel):
		if questionLevel == QuestionLevel.EASY:
			self.__player.points += __POINTS_FOR_EASY_QUESTION
		elif questionLevel == QuestionLevel.MEDIUM:
			self.__player.points += __POINTS_FOR_MEDIUM_QUESTION
		elif questionLevel == QuestionLevel.HARD:
			self.__player.points += __POINTS_FOR_HARD_QUESTION
		else:
			self.__player.points += 5
	
	
	def __readQuestions(self):
		with open('data/questions.csv', newline='') as questionsCsvFile:
			reader = csv.DictReader(questionsCsvFile)
			for row in reader:
				question = QuestionModel(id=row['id'], title=row['title'], level=row['level'])
				self.__questionsList.append(question)
	
	def __readQuestionAlternativesList(self, questionId):
		with open('data/alternatives.csv', newline='') as alternativesCsvFile:
			reader = csv.DictReader(alternativesCsvFile)
			self.__currentQuestionAlternativesList = []
			for row in reader:
				if row['question_id'] == questionId:
					alternative = AlternativeModel(id=row['id'], questionId=row['question_id'], title=row['title'], isCorrect=row['is_correct'])
					self.__currentQuestionAlternativesList.append(alternative)