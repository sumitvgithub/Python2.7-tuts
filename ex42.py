### Is-A, Has-A, Objects and Classes
 
# This is a weird concept, but to be very honest you only have to worry about it when you make new classes, and when you use a class. I will show you two tricks to help you figure out whether something is a class or object.

# First, you need to learn two catch phrases "is-a" and "has-a." 
# You use the phrase is-a when you talk about objects and classes being related 
# to each other by a class relationship. 
# You use has-a when you talk about objects and classes that are related only 
# because they reference each other.

# Remember, is-a is the relationship between Fish and Salmon, while has-a is the 
# relationship between Salmon and Gills.

# Animal is-a object
class Animal(object):
	pass

# Dog is-a Animal
class Dog(Animal):
	
	def __init__(self, name):
		# Dog has-a name 
		self.name = name
		
# Cat is-a Animal
class Cat(Animal):
	
	def __init__(self, name):
		# Cat has-a name
		self.name = name
		
# Person is-a object
class Person(object):
	def __init__(self, name):
		# Person has-a name
		self.name = name
		
		## Person has-a pet of some kind
		self.pet = None 	# What is the point of self.pet = None?
							# That makes sure that the self.pet attribute of 
							# that class is set to a default of None.
							# If written, 'self.pet' (without quotes) only, 
							# i.e. without assigning it 'None', then if we run 
							# the script from terminal, it would give error:
							# AttributeError: 'Person' object has no attribute 'pet'
							# Thus, one cannot write attributes without assigning
							# it anything in a class in a function.
							
# Employee is-a Person
class Employee(Person):

	def __init__(self, name, salary):
			# That's how you can run the __init__ method of a parent class reliably.
			# It means, call the parent class of Employee i.e. class Person and its 
			# __init__ method, i.e. Person's __init__ method with Employee's 'name'
			super(Employee, self).__init__(name)
			# Employee has-a salary
			self.salary = salary
			
# Fish is-a object
class Fish(object):
	pass
	
# Salmon is-a Fish
class Salmon(Fish):
	pass
	
# Halibut is-a Fish
class Halibut(Fish):
	pass
	
# rover is-a Dog
rover = Dog("Rover")
print rover			# on terminal, displays something like-->>
					# <__main__.Dog object at 0x02FC4730>
print rover.name	# on terminal, displays-->>	 Rover

# satan is-a Cat
satan = Cat("Satan")
print satan			# on terminal, displays something like-->>
					# <__main__.Cat object at 0x03244750>
print satan.name	# on terminal, displays-->>	Satan

# mary is-a Person
mary = Person("Mary")
print mary.name
print mary.pet

# From mary, get the pet attribute and set it to satan
mary.pet = satan
print mary.pet 

# set frank to an instance of class Employee and call it with Frank and 120000 
# parameters
frank = Employee("Frank", 120000)
print frank.name
print frank.salary
print frank.pet

# From frank, get the pet attribute and set it to rover
frank.pet = rover 	# It will go to class 'Employee', see 
					# " super(Employee, self).__init__(name) " which will call
					# class 'Person' (since 'super' is there), and set attribute 
					# 'pet' inside __init__ of class 'Person' to rover i.e. Rover
print frank.pet
					
# Set flipper to an instance of class Fish				
flipper = Fish()
print flipper

# Set crouse to an instance of class Salmon
crouse = Salmon()
print crouse

# Set harry to an instance of class Halibut
harry = Halibut()
print harry
# __________________________________________________________________--
# doc for 'super' and things to know about function 'super' 
# Source: http://www.artima.com/weblogs/viewpost.jsp?thread=236275