# More strings and text

x = "There are %d types of professionals" % 10  # This is plugging the number in % of the sentence.
teach = "how to teach"  # This variable binary is equal to the binary.
doNot = "who don't"  # This variable doNot is equal to don't.
y = "Those who know %s and those who %s" % (teach, doNot)  # This is plugging in the binary and doNot variable into %s.

print(x)  # This will print the x variable with 10 for %d.
print(y)  # This will print the y variable holding the plugged in variables in parenthesis.

print("I said: %r." % x)  # This print out the variable plugged in the %r of the sentence.
print("I also said: '%s'." % y)  # This print out variable plugged in the %s of the sentence.

fun = True  # Hilarious is equal to True statement.
funEvaluation = "How is that fun?! %r"  # The variable equals to the string with the %r (plugged in specifier)

print(funEvaluation % fun)  # This print out the latter after the prior sentence is formed.

w = "This is the left side of..."  # W equals to the string.
e = "a string with a right side."  # E equals to string.
print(w + e)  # Print out the two variables within the parenthesis and add them to make a sentence.

# More printing fun
print("Once upon a time...")  # Print out Mary string
print("There was something brilliant as %s." % 'snow')  # Print out metaphoric string
print("They found nature upon their travel and make a snow fort.")  # Print out Mary's destination
print("." * 10)  # Print out dots 10 times to make a line
end1 = "C"  # end1 equals to C
end2 = "h"  # end2 equals to h
end3 = "e"  # end3 equals to e
end4 = "e"  # end4 equals to e
end5 = "s"  # end5 equals to s
end6 = "e"  # end6 equals to e
end7 = "B"  # end7 equals to B
end8 = "u"  # end8 equals to u
end9 = "r"  # end9 equals to r
end10 = "g"  # end10 equals to g
end11 = "e"  # end11 equals to e
end12 = "r"  # end12 equals to r

print(end1 + end2 + end3 + end4 + end5 + end6)  # Print out end1, end2, end3, end4, end5, and end6 together.
print(end7 + end8 + end9 + end10 + end11 + end12)  # Print out end7, end8, end9, end10, end11, and end12 together.

# But wait! There's more:
formatter = "%r %r %r %r"
print(formatter % (5, 10, 15, 20))
print(formatter % ("five", "ten", "fifteen", "twenty"))
print(formatter % (True, False, False, True))
print(formatter % (formatter, formatter, formatter, formatter))

# Why do I use %r instead of %s in the above example?
# %r is returning the result that can be used to recreate the object it represents, becoming a format specifier in the Python syntax and logging and debugging the output.

# Which should I use on regular basis?
# I should use %s on regular basis because of their variables tying into the % or non-quotable format. Thus, it can spell out words from the function.

# Why does %r sometimes give me single quotes around things?
# It is to produce a representation of a Python object that is also valid Python source code, so it would be easier to read by using double quotes by itself. With double quotes or other cases, there would be single quotes.

names = "Fred Conner Julian April Nick Hyung"
process = "tree\nfood\napple\nboiling\npeeling\nchopping\ntossing\neating"

print("Here are the names:", names)
print("Here are the process:", process)

print("""
There's something going on here.
With the three double-quotes.
We'll be able to type as much as we like.
Even 4 lines if we want, or 5, or 6.
""")

# examine closely the differences between the %r formatter and %s formatter
print("These are the last names: %r" % names)
print("These are the last names: %s" % names)

# escape sequences redux
tabbyCat = "\tI'm tabbed in."
persianCat = "I'm split\non a line."
backslashCat = "I'm \\ a \\ cat."
topCat = """
I'll do a list:
\t* Cat Food
\t* Fishies
\t* Catnip\n\t* Grass
"""

print(tabbyCat)
print(persianCat)
print(backslashCat)
print(topCat)

# Escape Seq            What it does?
# \\                    Prints Backslash
print("I'm\\sleepy.")
# \'                    Prints single-quote
print("\'")
# \"                    Prints double quote
print("\"")
# \a                    Bell alert sounds
print("\a")
# \b                    Backspace removes previous character
print("You" + "\b" + "Go.")
# \f                    Formfeed
print("jump\fbackward")
# \n                    Linefeed
print("jump\nbackward")
# \N{name}              Prints characters from database
print(u"\N{DAGGER}")
# \r                    Moves all characters after the beginning of the line to next line.
print("6543\rOO_XX")
# \t                    Prints TAB
print("\t*wonderful")
# \uxxxx                Print 16-bit
print(u"\u1022")
# \Uxxxxxxxx            Prints 32-bit
print(u"\U000001a9")
# \v                    \x0b, formfeed
print("\v")
# \ooo                  Prints character based on octal value
print("\x091")
# \xhh                  Prints character based on hex value
print("\x23")

# What does the following code do:
#   While True:
#       for i in ["/", "-", "|", "\\", "|"]:
#           print("%s\r" % i, end='')

#   Can you use ''' instead of """ ?

age = input("How old are you?")
height = input("How tall are you?")

print("So, you are %r old and %r tall." % (age, height))

money = input("How much money would you want?")
spend = input("How much would you spend?")

print("So, you want %r dollars and %r to spend." % (money, spend))

food = input("What would you make today?")
time = input("What time would they be in?")

print("So, you want to make %r and %r in this day." % (food, time))

math = input("What did you learn in math today?")
example = input("Could you type them out?")

print("So, you learn %r and %r." % (math, example))

game = input("What do you like to play during your free time? One answer only.")
summary = input("What's the summary of them?")

print("So, you like to play %r and to %r during your free time." % (game, summary))





# making a story

print("What would be the story today?")
print("In 32000 BC, the Quo and the Gu were in conflict in between the territories. As part of that conflict, you were assigned to a group that had unique powers such as TYPES.")
gender = input("Are you a boy or a girl?")
print("So, you are %r" % (gender))
name = input("Your name is:")
print("Your name is:" % (name))
print("You boarded the ship of the Gu. Your Quo teammate brandished her sleeves, keeping her hair in a tight bun.")
ask = input("What do you remember?")
print("" % ask)
print("Do not forget the protocols, %r. Do not touch any SHINY because they have the potential to be stronger than ourselves. Well? Let's go defeat that Gu machinery!" % (name))
print("An alarm set off just when you arrived at the seating area. Someone had been expecting your group to break in?")
print("It's a trap!")
print("A great Gu machine is shaped like a human, brandishing its trademark company's name. Ren.")
print("Your other teammate shook their head at their teammates and ran on ahead. You tried to stop them, but the strange Gu machine stopped you by putting a great trail of flame in front of you.")
print("Do not interrupt Master with your friend's battle. It's the battle between the last Quo and Gu.")
print("As the Gu machinery aimed its tail at you, you nodded off...")
print("You woke up, finding yourself in a mess of the ruby and golden colored plated armor. You are the enemy of Quo.")
print("Wake up, %r! It's time for your daily check in the Ruby ship!" % (name))
print("Your AI, in a form of an ice cream, chirped.")
print("You went to the backroom where the storage units are. You feel guilt bubbling in your stomach. This time, the world is still 32000 BC, but there's something different, %r" % (name))
print("The actual civilization is asleep in your sword. The disruption between time and space is too great to contain, and %r sacrificed your old lineage to live." % (name))