# mostFrequentDigit(n) [10pts]
# Write the function mostFrequentDigit(n), that takes a non-negative integer n and returns the digit from 0 to 9 
# that occurs most frequently in it, with ties going to the smaller digit.

def mostfrequentdigit(n):
	# your code goes here
	n = str(n)

	if(len(n) == 1):
		return n
	elif(len(n) == 2):
		if(n[0] <= n[1]):
			return int(n[0])
		else:
			return n[1]	
	else:
		intial = -1
		c = 0
		for i in range(len(n)-1):
			if(n[i] == n[i+1]):
				intial = n[i]
				c = c+1
		if c>0:
			return int(intial)					