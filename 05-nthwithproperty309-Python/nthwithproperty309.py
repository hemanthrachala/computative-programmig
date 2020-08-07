# nthWithProperty309(n) [20 pts]
# We will say that a number n has "Property309" if its 5th power contains every 
# digit (from 0 to 9) at least once. 309 is the smallest number with this property. 
# Write the function nthWithProperty309 that takes a non-negative int n and returns 
# the nth number with Property309.

def iswith309(num):
	i = 0
	num = num**5
	temp = num
	c = 0

	while num > 0:

		if i != num % 10:
			num = num // 10
		elif i == num % 10:
			c += 1
			num = temp
			i += 1 
			if c > 9:
				return True
			return False	 	

def nthwithproperty309(n):
	# Your code goes here
	num = n
	i = -1
	guess = 0

	while i < num :
		guess += 1

		if iswith309(guess):
			i += 1
	return guess		
