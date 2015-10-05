### Build MadLibs Reverse Game ###
# STEPS #
# if answered correctly sentence refreshes with correct answer in place #

### RESOURCES ###
# python mad lib youtube https://www.youtube.com/watch?v=Oq75BBqd2y0

### User selects difficulty

#Global Variables#
difficulty = ""
easy = "The programming __1__ known as __2__ is an interpreted __1__. That means the __3__ executes instructions directly without compiling into machine-__1__ instructions. Also, __2__ is an interactive and __4__-oriented __1__."
medium = "A __5__ __6__ repeats a statment while a given condition is __7__. A __8__ __6__ is used to repeat code n __9__ of times. Please note, __6__s break by using the __10__ command."
hard = "A __11__ is a block of organized, reusable __12__ that is used to perform a single, related action. A __11__ __13__ begins with the __14__ __15__ followed by the __11__ name and __16__. Any __17__ should be placed within the __16__."

# easy = "easy"
# medium = "medium"
# hard = "hard"

#replaceMe = ["__" + str(questionNumber) + "__"]
answersToQuestions = ["language", "Python", "program", "object", "while","loop","True","for","number","return","function","code","block","keyword","def","parentheses","parameters"]
print answersToQuestions
print len(answersToQuestions)

#print replaceMe

print "What difficulty would you like to play?"
def difficultySelector(difficulty):
	difficulty = input("easy, medium, or hard: ")
	if difficulty == easy:
		print easy
	elif difficulty == medium:
		print medium
	elif difficulty == hard:
		print hard
	answerSelector(difficulty)

def answerSelector(difficulty):
	#print difficultySelector(difficulty)
	if difficulty == easy:
		answer = 0
		questionsToAnswer = 4
	elif difficulty == medium:
		answer = 4
		questionsToAnswer = 10
	elif difficulty == hard:
		answer = 10
		questionsToAnswer = 17
	askAndAnswerQuestions(difficulty, answer, questionsToAnswer)

def askAndAnswerQuestions(difficulty, answer, questionsToAnswer):
	while answer < questionsToAnswer:
		user_input = raw_input("Which word replaces number " + str(answer + 1) + "?: ")
		if user_input == answersToQuestions[answer]:
			## Update sentence with replaced answer ##
			print  difficulty.replace("__" + str(answer+1) + "__", answersToQuestions[answer])
			answer += 1
		else:
			print "Try again"
			answer = answer

# Run the program #
difficultySelector(difficulty)
