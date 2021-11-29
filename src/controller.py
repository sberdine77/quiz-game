import csv
import random
from typing import List
from models.question_model import QuestionModel, QuestionLevel
from models.alternative_model import AlternativeModel
from models.ranking_model import RankingModel

class Controller():
	def __init__(self, playerName):
		#Constants
		self.__POINTS_FOR_EASY_QUESTION = 10
		self.__POINTS_FOR_MEDIUM_QUESTION = 20
		self.__POINTS_FOR_HARD_QUESTION = 30

		#Variables
		self.__questionsList = []
		self.__currentQuestionAlternativesList = []
		self.__ranking = []

		self.__player = RankingModel(name=playerName)

	#Public method which returns a list of questions based on the number of wanted questions
	def getQuestionsList(self, wantedNumberOfQuestions) -> List[QuestionModel]:
		randomListOfNumbers = random.sample(range(0, 15), wantedNumberOfQuestions)
		self.__readQuestions(listOfWantedRows=randomListOfNumbers)
		return random.sample(self.__questionsList, len(self.__questionsList))
	
	#Public method which return a list of alternatives for the current question
	def getcurrentQuestionAlternativesList(self, questionId) -> List[AlternativeModel]:
		self.__readQuestionAlternativesList(questionId=questionId)
		return self.__currentQuestionAlternativesList
	
	'''Public method which adds the right number of points to the player
	depending on the level of the question
	'''
	def addPointsForQuestion(self, questionLevel: QuestionLevel):
		if questionLevel == QuestionLevel.EASY:
			self.__player.points += self.__POINTS_FOR_EASY_QUESTION
		elif questionLevel == QuestionLevel.MEDIUM:
			self.__player.points += self.__POINTS_FOR_MEDIUM_QUESTION
		elif questionLevel == QuestionLevel.HARD:
			self.__player.points += self.__POINTS_FOR_HARD_QUESTION
		else:
			self.__player.points += 5

	#Public method which ends the game
	def endGame(self):
		self.__endGame()
	
	#Private method that writes the data on the ranking before efectivelly ending the game
	def __endGame(self):
		self.__questionsList = []
		self.__currentQuestionAlternativesList = []
		playerDic = self.__player.asDictionary()
		with open("./data/ranking.csv", newline='', mode='a+') as rankingCsvFile:
			writer = csv.DictWriter(rankingCsvFile, fieldnames=['name', 'points'])
			#writer.writeheader()
			writer.writerow(playerDic)
			rankingCsvFile.close()
	
	'''Private method which reads the questions from the csv file and
	stores them in a class variable'''
	def __readQuestions(self, listOfWantedRows):
		with open('./data/questions.csv', newline='', encoding='utf-8') as questionsCsvFile:
			reader = csv.DictReader(questionsCsvFile)
			for i, row in enumerate(reader):
				if i in listOfWantedRows:
					question = QuestionModel(id=row['id'], title=row['title'], level=row['level'])
					self.__questionsList.append(question)
			questionsCsvFile.close()
	
	'''Private method which reads the alternatives of a question from the csv 
	file and stores them in a class variable'''
	def __readQuestionAlternativesList(self, questionId):
		with open('./data/alternatives.csv', newline='', encoding='utf-8') as alternativesCsvFile:
			reader = csv.DictReader(alternativesCsvFile)
			self.__currentQuestionAlternativesList = []
			for row in reader:
				if row['question_id'] == questionId:
					alternative = AlternativeModel(id=row['id'], questionId=row['question_id'], title=row['title'], isCorrect=row['is_correct'])
					self.__currentQuestionAlternativesList.append(alternative)
			alternativesCsvFile.close()
	
	#Public method which returns the ranking ordered by points
	def getRanking(self):
		self.__readRanking()
		return sorted(self.__ranking, key=lambda element: int(element.points), reverse=True)[:10]
	
	'''Private method which reads the ranking data from csv data and stores the
	result in a class variable'''
	def __readRanking(self):
		with open('./data/ranking.csv', newline='', encoding='utf-8') as rankingCsvFile:
			reader = csv.DictReader(rankingCsvFile)
			self.__ranking = []
			for row in reader:
				player = RankingModel(name=row['name'], points=int(row['points']))
				self.__ranking.append(player)
			rankingCsvFile.close()