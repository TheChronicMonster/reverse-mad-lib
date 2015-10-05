### Build MadLibs Reverse Game ###
# STEPS #

# Create a statement asking for difficulty #
# Make if statement selecting difficulty #
# Create sentences with blanks #
# Create a function to search through sentences #
# Create a try again prompt #
# if answered correctly sentence refreshes with correct answer in place #

### RESOURCES ###
# python mad lib youtube https://www.youtube.com/watch?v=Oq75BBqd2y0

### User selects difficulty

#Global Variables#

__1__ = "" # "language"
__2__ = "" # "Python"
__3__ = "" # "program"
__4__ = "" # "object"
__5__ = "" # "while"
__6__ = "" # "loop"
__7__ = "" # "True"
__8__ = "" # "for"
__9__ = "" # "number"
__10__ = "" # "return"
__11__ = "" # "function"
__12__ = "" # "code"
__13__ = "" # "block"
__14__ = "" # "keyword"
__15__ = "" # "def"
__16__ = "" # "parentheses"
__17__ = "" # "parameters"
difficulty = ""
easy = ""
medium = ""
hard = ""


#replaceMe = ["__" + str(questionNumber) + "__"]
answersToQuestions = ["language", "Python", "program", "object", "while","loop","True","for","number","return","function","code","block","keyword","def","parentheses","parameters"]
print answersToQuestions
print len(answersToQuestions)


#print replaceMe

print "What difficulty would you like to play?"
def difficultySelector():
	easy = ["easy", "EASY", "Easy"]
	medium = ["medium", "MEDIUM", "Medium"]
	hard = ["hard", "HARD", "Hard"]
	difficulty = input('easy, medium, or hard: ')
	if difficulty == easy:
		easyChallenge()
		answerSelector()
	elif difficulty == medium:
		mediumChallenge()
		answerSelector()
	elif difficulty == hard:
		hardChallenge()
		answerSelector()
	else:
		difficultySelector()

def answerSelector():
	if difficulty == easy:
		answer = 0
		questionsToAnswer = [__1__, __2__, __3__, __4__]
	elif difficulty == medium:
		answer = 4
		questionsToAnswer = [__5__, __6__, __7__, __8__, __9__, __10__]
	elif difficulty == hard:
		answer = 10
		questionsToAnswer = [__11__, __12__, __13__, __14__, __15__, __16__, __17__]
	while answer < len(questionsToAnswer):
		user_input = raw_input("What should replace " + answersToQuestions[answer] + "?")
		if user_input == answersToQuestions[answer]:
			answer += 1
		else:
			answer = answer



def easyChallenge():
	print """The programming __1__ known as __2__ is an
	interpreted __1__. That means the __3__ executes
	instructions directly without compiling into 
	machine-__1__ instructions. Also, __2__ is 
	an interactive and __4__-oriented __1__."""

#def easyAnswers():
#	if input == 
	# __1__ = "language"
	# __2__ = "Python"
	# __3__ = "program"
	# __4__ = "object"

def mediumChallenge():
	print """A __5__ __6__ repeats a statment while a given
	condition is __7__. A __8__ __6__ is used to
	repeat code n __9__ of times. Please note, __6__s break by using the
	__10__ command."""


def hardChallenge():
	print """A __11__ is a block of organized, 
	reusable __12__ that is used to perform a single, related action. 
	A __11__ __13__ begins with 
	the __14__ __15__ followed by the __11__ name and __16__. 
	Any __17__ should be placed with the __16__."""


# Run the program #
difficultySelector()
