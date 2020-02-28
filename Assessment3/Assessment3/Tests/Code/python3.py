    # Write a function to randomly generate a list with 5 even numbers between 100 and 200 inclusive.
    
    # For Example:
    
    # listGen() → [100,102,122,198,200]
    # listGen() → [108,104,106,188,200]
    # listGen() → [154,102,132,178,164]
import random

def listGen():
	l=[]
	while len(l) < 5:
		r = random.randint(100,200)
		if r % 2 == 0:
			l.append(r)
		else:
			r = random.randint(100,200)
			continue
	return l





    # Given an Array of Strings, remove any duplicate Strings that occur, then return the Array.
    # do not ignore case.

    # For Example:

	# removeDupe(["Dog"]) → ["Dog"]
	# removeDupe(["Dog","Cat"]) → ["Dog","Cat"]
	# removeDupe(["Dog","Dog","Cat"]) → ["Dog","Cat"]
    # removeDupe(["Dog","DoG","Cat"]) → ["Dog","DoG","Cat"]    

def removeDupe(input):
	ptr = 0
	counter = 0
	match = 0
	while ptr <= len(input):
		if 

	

    # Write a function which, given a string input, returns a string which contains only the characters with odd indexes.

	# For Example:

	# oddLetters("Hello") → "el"
	# oddLetters("hi") → "i"
	# oddLetters("0H1e2l3l4o5w6o7r8l9d") → "Helloworld"

def oddLetters(input):
	return ""

    # given a string - return the number of times "am" appears in the String
	# ignoring case -
	# BUT ONLY WHEN the word "am" appears without being followed or preceded by
	# other letters
	    
    # For Example:

	# amISearch("Am I in Amsterdam") → 1
	# amISearch("I am in Amsterdam am I?") → 2
	# amISearch("I have been in Amsterdam") → 0

def amISearch(arg1):
	return 0

    # Write a function which checks the validity of a credit card number.
	# The function will take a string and should return a boolean, True if the card is valid, or False if it is not.

	# A credit card has a valid number if it satisfies the following criteria.
	# - it must start with a 4, 5 or 6.
	# - it must contain exactly 16 digits.
	# - each digit must be 0-9 inclusive.
	# - it may contain hyphens ("-"), to separate groups of 4 digits only, but it cannot contain any other characters.
	# - it must not have 4 or more consecutive repeated digits.

	# For Example:

	# validCard(0123-4567-8901-2345) → False
	# validCard(401234567890123) → False
	# validCard(4012 3456 7890 1234) → False
	# validCard(4444-0123-4567-8901) → False
	# validCard(4012-3456-7890-1234) → True
	# validCard(4012345678901234) → True

def validCard(input):
	return False

    # Given an email address person@company.com, and a parameter "person" or "company",
	# write a function which returns the corresponding piece of information.
	# Your function should ignore case.

	# For Example:

	# email("john@google.com", "person") → john
	# email("jane@Microsoft.com", "company") → microsoft
	# email("Dave@amazon.com", "person") → dave

def email(email, parameter):
	return ""

    # Given a string, return the length of the largest "block" in the string.
	# A block is a run of adjacent chars that are the same, do not ignore case.
	
    # For Example:
	
	# superBlock("hoopplla") → 2
	# superBlock("abbCCCddDDDeeEEE") → 3
	# superBlock("") → 0
    
def superBlock(input):
	return -1

    # There is a mathematical function which is defined in the following way:

	# f(n)=0 if n=0
	# f(n)=1 if n=1
	# f(n)=f(n-1)+f(n-2) if n>1

	# eg f(2) = f(1) + f(0) = 1 + 0 = 1, so f(2) = 1

	# Write a Python function which outputs the result of the mathematical function, given an input n.

	# For Example:

	# f(3) → 2
	# f(8) → 21
	# f(0) → 0
	# f(1) → 1

def f(n):
	return 0

    # Write a function which solves the following puzzle.
	
	# We count 35 heads and 94 legs among the chickens and rabbits in a farm. How many rabbits and how many chickens do we have?
	# The values for 'heads' and 'legs' will be inputs and can be different from 35 and 94.
	# The output should be of the form (chickens,rabbits).
	# If there are no solutions to the puzzle, return "no solutions"

	# For Example:

	# headsLegs(35, 94) → (23, 12)
	# headsLegs(2, 6) → (1,1)
	# headsLegs(12,63) → "no soltuions"

def headsLegs(heads,legs):
	return "no solutions"

	# Given a string, return the boolean True if it ends in "py", and False if not. Ignore Case.

	# For Example:

	# endsDev("ilovepy") → True
	# endsDev("welovepy") → True
	# endsDev("welovepyforreal") → False
	# endsDev("pyiscool") → False
    
def endsPy(input):
	return False