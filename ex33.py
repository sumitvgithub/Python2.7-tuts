# While Loops 

i = 0
numbers = []

while i < 6:
	print "At the top i is %d" % i
	numbers.append(i)
	
	i = i + 1
	print "Numbers now: ", numbers
	print "At the bottom i is %d" % i
	
print "The numbers: "

for num in numbers:
	print num
	
print "________________________________________________________"

# -----------------------------------------------------

# Study Drills
# (1) Convert this while-loop to a function that you can
# call, and replace 6 in the test (i < 6) with a variable.
i = 0
j = 6
numbers = []

def fun(i):
	print "At the top i is %d" % i
	numbers.append(i)
	i = i + 1
	print "Numbers now: ", numbers
	print "At the bottom i is %d" % i

while (i < j):
	fun(i)
	i = i + 1
	
print "________________________________________________________"

# __________------------------------------------_____________

# Study Drills:
# (2) Write it to use for-loops and range. Do you need the incrementor
# in the middle anymore? What happens if you do not get rid of it?

## Answer: If I do not get rid of the incrementor in the middle, 
## i.e. [i = i + 1] at line 57, then the output is same as the first program.
i = 0
numbers = []

for i in range(6):
	print "At the top i is %d" % i
	numbers.append(i)
	i = i + 1
	print "Numbers now: ", numbers
	print "At the bottom i is %d" % i