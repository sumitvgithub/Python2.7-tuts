# Reading files 
from sys import argv # sys is a package, and this phrase just says to get
					 # the argv feature from that package. 

script, filename = argv # unpack script name and filename (arguments inputted
						# at terminal) 

txt = open(filename) # open the filename and it return that is written 
					 # in 'filename' and stored into variable 'txt'

print "Here's a file %r" %filename 

print txt.read() # read is a function with no parameters. It reads the
				 # 'txt' and displays output of 'txt' in terminal
				 
# You give a file a command by using the . (dot or period), the name of the
# command (command also called functions or methods), and parameters. Just like
# with open and raw_input. The difference is that txt.read() 
# says, "Hey txt! Do your read command with no parameters!"

txt.close() # if I don't write close(), the file won't be closed. 
			# Also we can open the same file again. But then two same files will
			# be opened if close() not written. 
			# If close() written, and then again we open the same file, then 
			# we have opened only one file again and not have two same files 
			# opened at the same time.
			

# Same process again below

print "Type the filename again:" 
file_again = raw_input("> ")

txt_again = open(file_again)

print txt_again.read()
txt_again.close()

###  Why is there no error when we open the file twice?
### Python will not restrict you from opening a file more than once and
### sometimes this is necessary.
