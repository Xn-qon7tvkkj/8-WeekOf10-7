# More strings and text

x = "There are %d types of people" % 10 # This is plugging the number in % of the sentence.
binary = "binary" # This variable binary is equal to the binary.
doNot = "don't" # This variable doNot is equal to don't.
y = "Those who know %s and those who %s" % (binary, doNot) # This is plugging in the binary and doNot variable into %s.


print(x) # This will print the x variable with 10 for %d.
print(y) # This will print the y variable holding the plugged in variables in parenthesis.

print("I said: %r." % x) # This print out the variable plugged in the %r of the sentence.
print("I also said: '%s'." % y) # This print out variable plugged in the %s of the sentence.

hilarious = True # Hilarious is equal to True statement.
jokeEvaluation = "Isn't that joke so funny?! %r" # The variable equals to the string with the %r (plugged in specifier)

print(jokeEvaluation % hilarious) # This print out the latter after the prior sentence is formed.

w = "This is the left side of..." # W equals to the string.
e = "a string with a right side." # E equals to string.
print(w+e) # Print out the two variables within the parenthesis and add them to make a sentence.

# More printing fun
print("Mary had a little lamb.") # Print out Mary string
print("Its fleece was white as %s." % 'snow') # Print out metaphoric string
print("And everywhere that Mary went.") # Print out Mary's destination
print("." * 10) # Print out dots 10 times to make a line
end1 = "C" # end1 equals to C
end2 = "h" # end2 equals to h
end3 = "e" # end3 equals to e
end4 = "e" # end4 equals to e
end5 = "s" # end5 equals to s
end6 = "e" # end6 equals to e
end7 = "B" # end7 equals to B
end8 = "u" # end8 equals to u
end9 = "r" # end9 equals to r
end10 = "g" # end10 equals to g
end11 = "e" # end11 equals to e
end12 = "r" # end12 equals to r

print(end1 + end2 + end3 + end4 + end5 + end6) # Print out end1, end2, end3, end4, end5, and end6 together.
print(end7 + end8 + end9 + end10 + end11 + end12) # Print out end7, end8, end9, end10, end11, and end12 together.

# But wait! There's more:
formatter = "%r %r %r %r"
print(formatter % (1, 2, 3, 4))
print(formatter % ("one", "two", "three", "four"))
print(formatter % (True, False, False, True))
print(formatter % (formatter, formatter, formatter, formatter))