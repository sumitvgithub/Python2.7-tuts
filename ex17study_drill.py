## STUDY DRILL of ex17
# This script "ex17.py" is really annoying. There's no need to ask you before doing
# the copy, and it prints too much out to the screen. Try to make the script
# more friendly to use by removing features.
from sys import argv
from os.path import exists

script, from_file, to_file = argv

print "Does the %s exists? %r" %(to_file, exists(to_file)) # This LOC not necessary
raw_input("Hit RETURN to continue copying else CTRL+C to abort.") # not necessary 

indata = open(from_file).read()
out_file = open(to_file, 'w').write(indata)
print "Size of %s file is %d bytes" %(to_file, len(to_file)) # not necessary
print "File has been copied successfully!"