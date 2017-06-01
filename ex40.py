### Modules, Classes and Objects

# Python is called an "object-oriented programming language." This means there 
# is a construct in Python called a class that lets you structure your software 
# in a particular way. Using classes, you can add consistency to your programs 
# so that they can be used in a cleaner way.

# Keep this idea of "get X from Y" in your head, and now think about modules. You've 
# made a few so far, and you should know they are:

# 1) A Python file with some functions or variables in it ..
# 2) You import that file.
# 3) And you can access the functions or variables in that module with the . (dot) 
# operator. 
# Imagine I have a module that I decide to name mystuff.py and I put a 
# function in it called apple. (Go to mystuff.py)

			####### Modules Are Like Dictionaries



import mystuff
mystuff.apple()
print mystuff.tangerine

# Refer back to the dictionary, and you should start to see how this is similar to
# using a dictionary, but the syntax is different. Let's compare:

''' mystuff['apple']  ''' # get apple from dict

mystuff.apple() # get apple from module
mystuff.tangerine # same thing, its just a variable

print "_"*100
# ______________________________________________________________________

			##### Classes Are Like Modules

class MyStuff(object):
	
	def __init__(self):
		self.tangerine = "And now a thousand years between"
		
	def apple(self):
		print "I AM CLASSY APPLES!"

# Classes are like "mini-module"

# ______________________________________________________________________
			##### Objects are like Import

# If a class is like a "mini-module," then there has to be a similar concept 
# to import but for classes. That concept is called "instantiate", which is just 
# a fancy, obnoxious, overly smart way to say "create." When you instantiate a 
# class what you get is called an object.

# You instantiate (create) a class by calling the class like it's a function,
# like this:
thing = MyStuff()  # instantiate
thing.apple()
print thing.tangerine

## 1) Python looks for MyStuff() and sees that it is a class you've defined.

## 2) Python crafts an empty object with all the functions you've specified in
# the class using def.

## 3) Python then looks to see if you made a "magic" __init__ function, and if
# you have it calls that function to initialize your newly created empty object.

## 4) In the MyStuff function __init__ I then get this extra variable self, which is
# that empty object Python made for me, and I can set variables on it just like
# you would with a module, dictionary, or other object.

## 5) In this case, I set self.tangerine to a song lyric and then I've initialized
# this object. Now Python can take this newly minted object and assign it to the 
# thing variable for me to work with.

### That's the basics of how Python does this "mini-import" when you call a 
# class like a function. Remember that this is not giving you the class, 
# but instead is using the class as a blueprint for building a copy of that 
# type of thing.

		###             SUMMARY               ###

## 1) Classes are like blueprints or definitions for creating new mini-modules.

## 2) Instantiation is how you make one of these mini-modules and import it at 
# the same time. "Instantiate" just means to create an object from the class.

## 3) The resulting created mini-module is called an object and you then assign it 
# to a variable to work with it.
print "_"*100
# ______________________________________________________________________
			##### 	GETTING THINGS FROM THINGS		#####
			
''' mystuff['apple'] ''' # dict style

# module style
mystuff.apple()
print mystuff.tangerine

# class style
thing = MyStuff()
thing.apple()
print thing.tangerine
print "_"*100
# ______________________________________________________________________
# ______________________________________________________________________
				###### 		A FIRST CLASS EXAMPLE 		######
			
class Song(object):

	def __init__(self, lyrics):
		self.lyrics = lyrics
		
	def sing_me_a_song(self):
		 for line in self.lyrics:
			print line
	
happy_bday = Song(["Happy birthday to you",
					"I don't want to get sued",
					"So I'll stop right there"])
					
bulls_on_parade = Song(["They rally around the family",
						"With pockets full of shells"])
					
print happy_bday.lyrics					
happy_bday.sing_me_a_song()

bulls_on_parade.sing_me_a_song()

###############			COMMON STUDENTS QUESTIONS 		################
### Why do I need self when I make __init__ or other functions for classes?
# If you don't have self, then code like cheese = 'Frank' is ambiguous. That 
# code isn't clear about whether you mean the instance's cheese attribute, or a 
# local variable named cheese. With self.cheese = 'Frank' it's very clear you mean 
# the instance attribute self.cheese.
