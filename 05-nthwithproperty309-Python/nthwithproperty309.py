# nthWithProperty309(n) [20 pts]
# We will say that a number n has "Property309" if its 5th power contains every 
# digit (from 0 to 9) at least once. 309 is the smallest number with this property. 
# Write the function nthWithProperty309 that takes a non-negative int n and returns 
# the nth number with Property309.

def iswith309(num):
	pass

def nthwithproperty309(n):
	# Your code goes here
	num = n
	i = 0
	guess = 0

	while i < num :
		guess += 1

		if iswith309(guess):
			i += 1
	return guess		
