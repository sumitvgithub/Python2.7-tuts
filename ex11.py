# Asking questions. Taking input

print "What's your name?"
name = input() # takes input from user as if it were a python code.
			   # in terminal, doesn't take string as an input but 
			   # takes integer. 
			   
# DETAILED EXPLANATIONS
#1
''' raw_input collects the characters the user types and presents them as a
 string. input() doesn't just evaluate numbers but rather treats any input as
 Python code and tries to execute it. Knowledgeable but malicious user could
 type in a Python command that can even deleted a file. Stick to raw_input()
 and convert the string into the data type you need using Python's built in
 conversion functions.
Also input(), is not safe from user errors! It expects a valid Python
expression as input; if the input is not syntactically valid, 
a SyntaxError will be raised.
 '''
#2
'''raw_input() returns string values
while input() return integer values
For Example:

1.

x = raw_input("Enter some value = ")
print x
Output:

Enter some value = 123
'123'
2.

y = input("Enter some value = ") 
print y
Output:

Enter some value = 123
123
Hence if we perform x + x = It will output as 123123

while if we perform y + y = It will output as 246
'''


print "How old are you?",
age = int(raw_input()) # gets the number as a string from raw_input()
					   # then converts it to an integer using int().
print "How tall are you?",
height = raw_input()
print "How much do you weigh?",
weight = raw_input()

print "My name is %r. So you're %r years old, %r tall and %r kg's heavy." %(
name, age, height, weight)