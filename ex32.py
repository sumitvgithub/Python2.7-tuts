# Loops and Lists

the_count = [1, 2, 3, 4, 5]
fruits = ['apples','oranges', 'pears', 'apricots']
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']

# this first kind of for-loop goes through a list
for number in the_count:
	print "This is count: %d" % number
	
# same as above
for fruit in fruits:
	print "A fruits of type: %s" % fruit
	
#also we can go througb lists too
# notice we have to use %r since we don't know what's in it
for i in change:
	print "I got %r" % i
	
# we can also build lists, first start with an empty one
elements = []

# then use the range function to do 0 to 5 counts 
for i in range(0, 6):   # could've also used "range(6)".. means the same
 	print "Adding %d to the list." % i
	# append is a function lists understands
	elements.append(i)
	print elements
	
# now we can print them out too all together
for i in elements:
	print "Element was : %d" % i
	
# -------------------------------------------------------------- 

## Study Drill: Could you have avoided that for-loop entirely on line 22
## and just assigned range(0,6) directly to elements?
## Answer: Yes, Just write "elements = range(0, 6)" and "print elements"
## Output would be a list "[0, 1, 2, 3, 4, 5]"
## See below:
elements = range(0,6)
print elements

# ________________________________________________________
# Question: Append x = [1,2,3,4,5] with y = [9,7,0,3] and print as a 
# single list
x = [1,2,3,4,5]
y = [9,7,0,3]
for i in range(len(y)):
	print "\tElement %d" % i
	x.append(y[i])
print x

# ______________________________________________________________
# Question: Append x = [1,2,3,4,5] with itself and print as a single 
# list (and not print as [1,2,3,4,5,[...]]   ). [...] means appended
# same list to itself 
x = [1,2,3,4,5]
for i in range(len(x)):
	x.append(x[i])
print x

#############         OR          #######
x = [1,2,3,4,5]
for i in range(1,6):
	x.append(i)
print x

# if it was printed as [1,2,3,4,5,[...]] then code would've been
x = [1,2,3,4,5]
for i in range(0,1):
	x.append(x)
print x
print "----------------------------------"
# ________________________________________________________
#Reference for below: https://docs.python.org/3/tutorial/datastructures.html
# https://docs.python.org/3/library/collections.html#collections.deque
from collections import deque
x = deque([4,7,2,9])
# x.append(x)
# print x
x.extend(x)
print x
# x.insert(0,52)
# print x
# x.remove(2)
# print x
x.appendleft(x)
print x
print "No of occurences of 4: ", x.count(4)
# x.clear()
# print x
# x.pop()
x.reverse()
print x
# x.index(2)
x.remove(7)
print x
x.reverse()
print x

d = deque('ghi')
for elem in d:
	print elem.upper()
d.clear()
d.extendleft('123')
print d
d.extendleft('123')
print d