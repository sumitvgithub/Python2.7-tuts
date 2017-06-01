# Functions and Files
from sys import argv

script, input_file = argv

def print_all(f):
	print f.read()
	
def rewind(f):
	return f.seek(0) # if written 'print f.seek(0)' then in powershell after "Now let's rewind
					 # like a tape", it prints "None". To avoid that, use 'return' instead of 
					 # 'print'...It is because of recursion. Although I don't understand why 
					 # recursion is happening ...
	
def print_a_line(line_count, f):
	print line_count, f.tell(), f.readline(), # f.tell() asks the file for the current position
											  # Why are there empty lines between the lines
											  # in the file?
											  # The readline() function returns the \n that's
											  # in the file at the end of that line. Add a , at
											  # the end of your print function calls to avoid
											  # adding double \n to every line.

	#How does readline() know where each line is?
	#Inside readline() is code that scans each byte of the file until it finds a \n character,
	#then stops reading the file to return what it found so far. The file f is responsible for
	#maintaining the current position in the file after each readline() call, so that it will keep
	#reading each line.

current_file = open(input_file)

print "First let's print the whole file:\n"

print_all(current_file)

print "Now let's rewind like a tape."

rewind(current_file)

    #After rewinding, the file pointer is back at the start of the file. Each call to f.readline()
	#will read one line from f. After this the f's file pointer will be at the start of
	#the next line. Therefore, the program reads the lines consecutively.
	
print "Let's print three lines:"

current_line = 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)