# Doing Things to Lists

ten_things = "Apple Oranges Crows Telephone Light Sugar"
stuff = ten_things.split()
print stuff
print "Wait there are not 10 things in the list. Let's fix that."
more_stuff = ["Day", "Night", "Song", "Frisbee", "Corn", "Banana", "Girl", "Boy"]

while len(stuff) != 10:
	next_one = more_stuff.pop()
	print "Adding:", next_one
	stuff.append(next_one)
	print "There are %d item now." % len(stuff)
	
print "There we go:", stuff

print "Let's do some things with stuff."

print "stuff [1] prints: ", stuff[1]
print "stuff [-1] prints: ", stuff[-1]
print "stuff.pop() returns: ", stuff.pop()
print ' . '.join(stuff)
print ' # '.join(more_stuff)
print '#'.join(stuff[3:5])
