# Parameters, Unpacking and Variables
from sys import argv

script, first, second, third = argv

x = raw_input("What is your name?")
print "The script is called: ", script 
print "Your first variable is:", int(first) # terminal will only accept integer
											# argument as input to variable 'first'
print "Your second variable is:", raw_input("What is it?"),second
									# can combine raw_input() and anything after that.
									# it will first take input from user, then 
									# print that input to terminal, then print 
									# variable 'second' output
print "Your third variable is:", third

print "My name is %s" %x

y = raw_input("What's the nearest restaurant?")
print "Nearest restaurant is %r" %y