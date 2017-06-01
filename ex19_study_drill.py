## STUDY DRILL : Write at least one more function of your own design, and run it
## 10 different ways.

def one_more(cups, plates, spoons, *args):
	print "We have %r cups, %r plates and %r spoons" %(cups, plates, spoons)
	a1, a2 = args
	print "There are 2 arguments, a1:%r and a2:%r\n" %(args)
	
c = 10; p = 20; s = 30

one_more(c, p, s, c+p, p+s)
c = raw_input()				# NOTE: raw_input() return string. So CAN take 
							# any other data-type as input as well.
p = int(raw_input())     # type cast the 'str' to 'int' and will take only 'int'
						 # as input
s = input()			# input() returns 'int' so no need to use int(raw_input())
					# and will only take 'int' as input from user
print type(c,p,s)#;print type(p);print type(s)
one_more(c, p, s, 66, 77)