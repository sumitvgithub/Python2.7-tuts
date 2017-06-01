## More Files (Reading and Writing, Copying files)
from sys import argv
from os.path import exists

script, from_file, to_file = argv

print "Copying from %s to %s" %(from_file, to_file)

#in_file = open(from_file)
#indata = in_file.read()

# Above two LOC can be combined in single line as below
indata = open(from_file).read()

print "The input file is %d bytes." %len(indata)

print "Does the file %s exist? %r" %(to_file,exists(to_file))
print "Ready, hit RETURN to continue and CTRL+C (^C) to abort."
raw_input()

out_file = open(to_file, 'w')
out_file.write(indata)

print "Alright, all done."

out_file.close()
# in_file.close() # Uncomment this LOC when Line 9 and 10 are uncommented and
				  # Line 13 is commented
				  # When done like,  indata = open(from_file).read(), 
				  # which means you don't need to then do in_file.close()
				  # when you reach the end of the script. It should already
				  # be closed by Python once that one line runs.
				  
### See ex27study_drill.py for shorter version of this (ex17.py) script 
### and ex17study_drill_1_LOC.py to write same script in only 1 LOC