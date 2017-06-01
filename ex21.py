# Functions can return something
def add(a,b):
	print "ADDING %d + %d" %(a,b)
	return a + b
	
def sub(a,b):
	print "SUBTRACTING %d - %d" %(a,b)
	return a - b
	
def multiply(a,b):
	print "MULTIPLYING %d * %d" %(a,b)
	return a * b
	
def divide(a,b):
	print "DIVIDING %d / %d" %(a,b)
	return a / b
	
print "Let's do some math with the functions!"

age = add(30,5)
height = sub(78,4)
weight = multiply(90,2)
iq = divide(100,2)

print "Age: %d, Height: %d, Weight: %d, IQ: %d"%(age, height,weight,iq)

# A puzzle for the extra credit 
print "Here is a puzzle."

what = add(age,sub(height, multiply(weight,divide(iq,2)))) # calculates from "inside out", inner 
														   # brackets first then outwards
														   
what = add(int(raw_input()),sub(int(raw_input()), multiply(int(raw_input()),divide(int(raw_input()),2))))
# This takes input from outward bracket first then inside then inside and so on, then calculates.
# i.e. here, takes input from left to right then  calls the function according to parenthesis order


print "That becomes: ", what, "Can you do it by hand?"
