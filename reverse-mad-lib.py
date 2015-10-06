### MadLibs Reverse Game ###

# It's not as fun as a crazy Mad Lib game, but is a bit more educational.

### RESOURCES ###
# UDACITY IPND Madlib Project 2
# python mad lib youtube https://www.youtube.com/watch?v=Oq75BBqd2y0

#Global Variables#
difficulty = ""
easy = "The programming __1__ known as __2__ is an interpreted __1__. That means the __3__ executes instructions directly without compiling into machine-__1__ instructions. Also, __2__ is an interactive and __4__-oriented __1__."
medium = "A __5__ __6__ repeats a statment while a given condition is __7__. A __8__ __6__ is used to repeat code n __9__ of times. Please note, __6__s break by using the __10__ command."
hard = "A __11__ is a block of organized, reusable __12__ that is used to perform a single, related action. A __11__ __13__ begins with the __14__ __15__ followed by the __11__ name and __16__. Any __17__ should be placed within the __16__."
special = "Now, this is a __18__ all about how My life got flipped-turned upside __19__ And I'd like to take a minute Just sit right there I'll tell you how I became the __20__ of a town called Bel Air In west __21__ born and raised On the playground was where I spent most of my __22__ Chillin' out maxin' relaxin' all cool And all shootin some __23__ outside of the school. When a couple of guys who were up to no good Started making trouble in my __24__ I got in one little fight and my mom got scared She said 'You're movin' with your auntie and uncle in __25__' I whistled for a cab and when it came near The license plate said fresh and it had dice in the mirror. If anything I could say that this cab was rare But I thought 'Nah, forget it' - 'Yo, homes to __25__' I pulled up to the house about 7 or 8 And I yelled to the cabbie 'Yo homes __26__ ya later' I looked at my kingdom I was finally there To sit on my throne as the __20__ of __25__"

answersToQuestions = ["language", "Python", "program", "object", "while","loop","True","for","number","return","function","code","block","keyword","def","parentheses","parameters","story","down","Prince","Philadelphia","days","b-ball","neighborhood","Bel Air","smell"]

# Difficulty input, prints message
print "What difficulty would you like to play?"
def difficultySelector(difficulty):
	difficulty = input("easy, medium, or hard: ")
	if difficulty == easy:
		print easy
	elif difficulty == medium:
		print medium
	elif difficulty == hard:
		print hard
	elif difficulty == special:
		print special
	answerSelector(difficulty)

# Selects which part of the array to use for answers
def answerSelector(difficulty):
	if difficulty == easy:
		answer = 0
		questionsToAnswer = 4
	elif difficulty == medium:
		answer = 4
		questionsToAnswer = 10
	elif difficulty == hard:
		answer = 10
		questionsToAnswer = 17
	elif difficulty == special:
		answer = 17
		questionsToAnswer = 26
	askAndAnswerQuestions(difficulty, answer, questionsToAnswer)

# sets up while loop which verifies user inputs per array while True
def askAndAnswerQuestions(difficulty, answer, questionsToAnswer):
	while answer < questionsToAnswer:
		user_input = raw_input("Which word replaces number " + str(answer + 1) + "?: ")
		if user_input == answersToQuestions[answer]:
			## Update sentence with replaced answer ##
			difficulty = difficulty.replace("__" + str(answer+1) + "__", answersToQuestions[answer])
			print difficulty
			answer += 1
		else:
			print "Try again"
			answer = answer

# Run the program #
difficultySelector(difficulty)
