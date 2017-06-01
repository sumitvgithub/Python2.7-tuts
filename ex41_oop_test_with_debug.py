### Learning To Speak Object Oriented
## A Reading Test

import random
from urllib import urlopen
import sys

WORD_URL = "http://learncodethehardway.org/words.txt"
WORDS = []

PHRASES = {
	"class %%%(%%%):":
		"Make a class named %%% that is-a %%%.",
	"class %%%(object):\n\tdef __init__(self, ***)":
		"class %%% has-a __init__ that takes self and *** parameters.",
	"class %%%(object):\n\tdef ***(self, @@@)":
		"class %%% has-a function named *** that takes self and @@@ parameters.",
	"*** = %%%()":
		"Set *** to an instance of class %%%.",
	"***.***(@@@)":
		"From *** get the *** function, and call it with parameters self, @@@.",
	"***.*** = '***'":
		"From *** get the *** attribute and set it to '***'."
}

# do they want to drill phrases first
if len(sys.argv) == 2 and sys.argv[1] == "english":
	PHRASE_FIRST = True
	print PHRASE_FIRST
else:
	PHRASE_FIRST = False
	print PHRASE_FIRST
	'''print "Name of the script: ", sys.argv[0]
	print "Number of arguments passed to the command line: ", len(sys.argv)
	print "The arguments passed to the command line are: ", str(sys.argv)'''
	
##### SOURCE: http://www.pythonforbeginners.com/system/python-sys-argv
# # What is sys.argv?
# # sys.argv is a list in Python, which contains the command-line arguments passed
# # to the script. 

# # With the len(sys.argv) function you can count the number of arguments. 

# # If you are gonna work with command line arguments, you probably want to 
# # use sys.argv. 

# # To use sys.argv, you will first have to import the sys module. 
# # Example
# # To show how this works. 

# # Remember that sys.argv[0] is the name of the script.

# # # import sys
# # # print "This is the name of the script: ", sys.argv[0]
# # # print "Number of arguments: ", len(sys.argv)
# # # print "The arguments are: " , str(sys.argv)
# # # Output
# # # This is the name of the script:  sysargv.py
# # # Number of arguments in:  1
# # # The arguments are:  ['sysargv.py']

# # # If I run it again with additional arguments, I will get this output:

# # # This is the name of the script:  sysargv.py
# # # Number of arguments in:  3
# # # The arguments are:  ['sysargv.py', 'arg1', 'arg2']


# load up the words from the website
for word in urlopen(WORD_URL).readlines():
	WORDS.append(word.strip()) # If I write simply WORDS.append(word) , then \n 
							   # would also be outputted on terminal with the words.
							   # for clarity, do check with WORDS.append(word)
							   
# .strip() removes all whitespace at the start and end, including spaces, tabs,
# newlines and carriage returns. Leaving it in doesn't do any harm, and allows
# your program to deal with unexpected extra whitespace inserted into the file.

print WORDS


def convert(snippet, phrase):
	class_names = [w.capitalize() for w in 
				   random.sample(WORDS, snippet.count("%%%"))]
				 # capitalize() method returns a copy of the string with only
				 # its first character capitalized.
	print "class_names-->>", class_names
	other_names = random.sample(WORDS, snippet.count("***"))
	print "other_names-->>", other_names
	results = []
	param_names = []
	
	for i in range(0, snippet.count("@@@")):
		param_count = random.randint(1,3)
		print "\n\tPARAM COUNT-->>", param_count
		param_names.append(', '.join(random.sample(WORDS, param_count)))
		print "\n\tPARAM NAMES-->>", param_names
		
	for sentence in snippet, phrase:    # first 'for loop' runs for sentence = snippet
										# then, when it finishes, it goes for-->>
										# 'for loop' for sentence = phrase
										# i.e. first iteration-> for sentence in snippet
										# next iteration-> for sentence in phrase
										
		result = sentence[:]	# What does result = sentence[:] do?
								# That's a Python way of copying a list. You're
								# using the list slice syntax [:] to effectively 
								# make a slice from the very first element to the 
								# very last one.
								
		print "\n\tRESULT-->>", result
		
		# fake class names
		for word in class_names:
			result = result.replace("%%%", word, 1)
			print "\n\tINSIDE FAKE CLASS NAMES-->>", result
			
		# fake other names	
		for word in other_names:
			result = result.replace("***", word, 1)
			print "\n\tINSIDE FAKE OTHER NAMES-->>", result
			
		# fake parameter lists
		for word in param_names:
			result = result.replace("@@@", word, 1)
			print "\n\tINSIDE FAKE PARAMETER LISTS-->>", result
			
		print "results.append(result)"
		results.append(result)

	print "--------------------------------",results
	return results

# keep going until they hit CTRL-D
try:
	while True:
		snippets = PHRASES.keys()
		random.shuffle(snippets)
		
		for snippet in snippets:
			print "\n\tSnippet-->>",snippet
			phrase = PHRASES[snippet]
			print "\n\t\tPhrase-->>",phrase
			question, answer = convert(snippet, phrase)
			if PHRASE_FIRST:
				question, answer = answer, question
			
			print "_"*100
			print question
			
			raw_input("> ")
			print "ANSWER: %s\n\n" % answer
			print "_"*100
except EOFError:
	print "\nBYE!"