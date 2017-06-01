## Escape sequences
tabby_cat = "\t I'm tabbed in"
persian_cat = "I'm split \non a line."
backslash_cat = "I'm \\ a \\ cat."

ascii_bell = "I'm a \a cat."      # \a adds extra space where \a is written
ascii_backspace = "I'm a \b cat." # \b removes the space where \b is written
ascii_formfeed = "I'm a \f cat."  # \f makes a rectangular box (dabba) kind of thing
# in powershell and a ? inside a box in cmd.

wow = "you there?"
combine = "Hello, this is \"%r sumit " % wow   # combine double-quotes escape with %r.
# output in double-quote of \"%r is included

# triple single-quotes also does the same thing as triple double-quotes.
# Follow whichever suits you.
fat_cat = '''            
I'll do a list.
\t* Cat food.
\t* Fishies.
\t* Catnip\n\t* Grass.
'''

print tabby_cat
print persian_cat
print backslash_cat
print fat_cat
print ascii_bell
print ascii_backspace
print ascii_formfeed
print combine


## Let's have some fun! Remove triple single-quotes for fun! ;)
'''
while True:
    for i in ["/","-","|","\\","|"]:
        print "%s\r" % i,

'''