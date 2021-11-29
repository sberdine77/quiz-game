from controller import Controller
import string

#Helper variable containing the lower-case alphabet
aZRange = string.ascii_lowercase[:26]

#Function which shows the alternatives in a aphabet-listed way
def showAlternatives(alternatives):
	alternativeNumber = 0
	for alternative in alternatives:
		print(f'\t{aZRange[alternativeNumber]}) {alternative.title}')
		alternativeNumber += 1

#Input helper which blocks invalid inputs for answers
def inputHelper(currentAlternatives):
	while True:
		answer = input()
		if answer == 'exit':
			return answer
		elif answer != 'exit' and answer not in aZRange:
			print("Please, insert valid answers (a-z or 'exit')")
		elif answer not in aZRange and answer != 'exit':
			print("Please, insert valid answers (a-z or 'exit')")
		elif (aZRange.index(answer) + 1) > len(currentAlternatives):
			print("Please, insert a letter that represents one of the questions alternatives")
		else:
			return answer

#Input helper which blocks invalid inputs for names
def getName():
	while True:
		answer = input()
		if answer == '':
			print("Please, insert a valid name")
		else:
			return answer

#Function which app points if the answer is correct
def checkAnswer(currentQuestion, currentAlternatives):
	response = inputHelper(currentAlternatives)
	if response == 'exit':
		return response
	elif currentAlternatives[aZRange.index(response)].isCorrect:
		myController.addPointsForQuestion(currentQuestion.level)
		return response

#Function which shows the ranking in a organized way
def showRanking():
	print("Ranking: ")
	rankingList = myController.getRanking()
	rankingNumber = 1
	for item in rankingList:
		print(f"{rankingNumber}) Player: {item.name}, Points: {item.points}")
		rankingNumber += 1

#Function which helps the user to decide if the games continues or not
def continueOrNot():
	while True:
		answer = input()
		if answer != 'y' and answer != 'n':
			print("Please, insert a valid answer")
		elif answer == 'y':
			return True
		elif answer == 'n':
			return False

#Start
while True:
	print("What's your name?")
	playerName = getName()
	myController = Controller(playerName=playerName)
	listOfQuestions = myController.getQuestionsList(15)

	print(f"\nWelcome {playerName}! Answer the questions with the letter representing one alternative or write 'exit' to end the game\n")

	#Showing questions and alternatives
	for question in listOfQuestions:
		currentAlternatives = myController.getcurrentQuestionAlternativesList(question.id)
		print(question.title)
		showAlternatives(currentAlternatives)
		response = checkAnswer(question, currentAlternatives)
		if response == 'exit':
			print('\n')
			break
		print('\n')

	myController.endGame()
	showRanking()
	print("You wish to continue for another match? (y / n)")
	if not continueOrNot():
		break
