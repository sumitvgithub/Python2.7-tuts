formatter = "%r %r %r %r"

print formatter % (1, 2, 3, 4)
print formatter % ("one", "two", "three", "four")
print formatter % (formatter, formatter, formatter, formatter)

# Notice the 2nd last line of output in powershell, that: 
# If there's a single-quote word (word is: didn't) inside a 
# double-quotted string then the output is inside a double-quote; 
# otherwise inside a single-quote.

print formatter % (
"I had this thing.",
"That you could type up right.",
"But it didn't sing.",
"So I said goodnight."
)