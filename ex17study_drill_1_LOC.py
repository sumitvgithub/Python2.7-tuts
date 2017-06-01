## Study Drill for ex17.py
# To copy one file to another in one LOC.
#No way you can make this one line!
## That ; depends ; on ; how ; you ; define ; one ; line ; of ; code.

from sys import argv; script, source, destination = argv; in_file = open(source).read(); out_file = open(destination, 'w').write(in_file)