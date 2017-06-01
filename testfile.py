from sys import argv
script, file, new = argv
#u_in=raw_input("Write whatever you want to write in %s file" %file)
#out = open(file).write(u_in) ## LOC at line3 and 4 uncommented when only 
							  ## script, file = argv
out = open(new,'w').write(open(file).read()) 