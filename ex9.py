## Printing, Printing, Printing

days = "Mon Tue Wed Thu Fri Sat Sun"
months = "Jan\nFeb\nMar\nApr\nMay\nJun\nJul\nAug"

print "Here are the days:  ", days
print "Here are the months:%r " %months #Why do the \n newlines not work when I use %r?
#That's how %r formatting works; it prints it the way you wrote it (or close to it). 
#It's the "raw" format for debugging.

print "Here are the months: ", months

print """
There's something going on here.
With the 3 double-quotes.
doesnt 
matter

if we leave a line.
We'll be able to type as much as we like.
Even 4 lines if we want, or 5, or 6.
"""