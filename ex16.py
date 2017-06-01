## Reading and Writing Files
from sys import argv

script, filename = argv

print "We're going to erase %r." %filename
print "If you don't want that, press CTRL+C (^C)."
print "If you do want that, press RETURN."

raw_input('?')

print "Opening the file..."
target = open(filename, 'w') # when mode 'w' used, it means
							 # writing (truncating the file
							 # if it already exists). 
							 # doing open(filename) open it in 'r' (read) mode.
							 # that's the default for the open() function.

print "Truncating the file. GoodBye!"
# target.truncate()          # No need to write truncate() 
							 # function as mode 'w' already 
							 # truncates the file if it exists

print "Now I'm going to ask you for three lines."

line1 = raw_input("line 1:")
line2 = raw_input("line 2:")
line3 = raw_input("line 3:")

print "I'm going to write these to the file."

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

''' target.write("%r\n%r\n%r\n" %(line1,line2,line3)) '''
					# Alternatively, you can print 
					# line1, line2, line3 using one write() call.
					
## NOTE: cannot write the above LOC as:
### target.write("%r\n%r\n%r\n") %(line1,line2,line3)
# Since, write() doesn't return anything, it will raise an error:
# -->TypeError: unsupported operand type(s) for %: 'NoneType'
# -->and 'tuple'
# You want to apply % to the string instead:
###  target.write("%r%r%r" %(line1,line2,line3))
# My errored code is applying it to the return value of 
# the write() call, which returns 'None'.
# Thus, don't write %(line1,line2,line3) outside write() call's
# bracket. 

print "And finally we close it."
target.close() 

target = open(filename) # cannot read the file using target.read() 
						# if line 56 of code not written(and Line58 code written),
						# i.e. if file not closed then, we cannot read the
						# file since at line 13, we've opened it in 'write'
						# mode and not in 'read' mode.
						## Summary, I cannot read a file when it is in 'write' mode
						## in the same script without closing it first
                        ## using close() at line56
print target.read()
target.close()