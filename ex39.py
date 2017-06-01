# Dictionaries, Oh Lovely Dictionaries

# create a mappinf of state to abbreviation
states = {
'Oregon': 'OR',
'Florida': 'FL',
'California': 'CA',
'New York': 'NY',
'Michigan': 'MI'
}

print "States are: \n", states

# create a basic set of states and cities in them
cities = {
'CA': 'San Francisco',
'MI': 'Detroit',
'FL': 'Jacksonville'
}

print "Cities are: \n", cities

# add some more cities
cities['NY'] = 'New York'
cities['OR'] = 'Portland'

# print out some cities
print '-' * 10
print "Michigan's abbreviation is: ", states['Michigan']
print "Florida's abbreviation is: ", states['Florida']

# do it by using the state then cities dict 
print '-' * 20
print "Michigan has: ", cities[states['Michigan']]
print "Florida has: ", cities[states['Florida']]

#print every state abbreviation
print '-' * 20
for state, abbrev in states.items():
	print "%s is abbreviated %s" % (state, abbrev)
	
# print every city in state
for abbrev, city in cities.items():
	print "%s has the city %s" % (abbrev, city)

# now do both at the same time
print '-' * 20
for state, abbrev in states.items():
	print "%s state is abbreviated %s and has city %s" % (state, abbrev,
	cities[abbrev])
	
print '-' * 20
# safely get a abbreviation by state that might not be there
state = states.get('Texas') ## if written state = states.get('Texas','Anything')
							## This means that if 'Texas' is in states else 'Anything'
	

if not state:
	print "Sorry, no Texas."
# get a city with a default values
city = cities.get('TX', 'Does not exist') ## if 'TX' in cities then print the city
										  ## corresponding to the abbreviation else
										  ## 'Does not exist'
print "The city for the state 'TX' is: %s" % city

city = cities.get('CA','Does not exist')
print "The city for the state 'CA' is: %s" % city ## will print city corresponding
												  ## to the abbreviation CA, i.e.,
												  ## San Francisco
print "_" *100


###############      COMMON STUDENTS QUESTIONS      #################


## What is the difference between a list and a dictionary?
# A list is for an ordered list of items. A dictionary (or dict) is for
# matching some items (called "keys") to other items (called "values").

## What would I use a dictionary for?
# When you have to take one value and "look up" another value. In fact you could
# call dictionaries "look up tables."

## What would I use a list for?
# Use a list for any sequence of things that need to be in order, and you only need
# to look them up by a numeric index.

## What if I need a dictionary, but I need it to be in order?
# Take a look at the collections.OrderedDict data structure in Python. Search for
# it online to find the documentation.


# ________________________________________________________________________________

### Source: https://docs.python.org/2/tutorial/datastructures.html#dictionaries

#### USE BELOW IN PYTHON SHELL...WON'T EXECUTE IN CMD.

# Here is a small example using a dictionary:

tel = {'jack': 4098, 'sape': 4139}
tel['guido'] = 4127
tel

tel['jack']

del tel['sape']
tel['irv'] = 4127
tel

tel.keys() # The keys() method of a dictionary object returns a list of 
		   # all the keys used in the dictionary, in arbitrary order
		   # (if you want it sorted, just apply the sorted() function to it).
		   # To check whether a single key is in the dictionary, use the in keyword.

'guido' in tel

# The dict() constructor builds dictionaries directly from sequences of key-value
# pairs:
dict([('sape', 4139), ('guido', 4127), ('jack', 4098)])

# In addition, dict comprehensions can be used to create dictionaries from
# arbitrary key and value expressions:
{x: x**2 for x in (2, 4, 6)}

# When the keys are simple strings, it is sometimes easier to specify pairs
# using keyword arguments:
dict(sape=4139, guido=4127, jack=4098)

# ________________________________________________________________________________

### Source: https://docs.python.org/3/library/collections.html#ordereddict-examples-and-recipes

from collections import OrderedDict

# regular unsorted dictionary
d = {'banana': 3, 'apple': 4, 'pear': 1, 'orange': 2}

# dictionary sorted by the key
print OrderedDict(sorted(d.items(), key = lambda t: t[0] ))

# dictionary sorted by the value
print OrderedDict(sorted(d.items(), key = lambda t: t[1] ))

# dictionary sorted by the length of the key string
print OrderedDict(sorted(d.items(), key = lambda t: len(t[0]) ))