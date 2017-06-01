## More Variables and Printing
name = 'Sumit Verma'
age = 19
inches = 12.0 # 1 ft = 12 in
pound = 2.2 # 1 kg = 2.2 pound

height = 5.3 # in feet. 
weight = 56.0 # in kgs
eyes = 'Black'
teeth = 'White'
hair = 'Black'

print "Let's talk about %s." %name
print "He's %d years old." %age
print "He's %f ft tall." %height
print "So, He's %f inches tall." %(height*inches)
print "He's %f kg's heavy." %weight
print "So, He's %f pounds heavy." %(weight*pound)
print "He's got %s eyes and %s hair." %(eyes,hair)
print "His teeth are %s depending on the coffee." %teeth

print "If I add %f, %f and %f I get %f." %(age, height, weight, age + height + weight) 