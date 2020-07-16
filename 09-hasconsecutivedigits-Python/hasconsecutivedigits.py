# hasConsecutiveDigits(n)  [10pts]
# Write the function hasConsecutiveDigits(n) that takes a possibly negative int value n and returns True if that 
# number contains two consecutive digits that are the same, and False otherwise.

def hasconsecutivedigits(n):
	# your code goes here
	num = str(abs(n))

	prev = -1

	for i in range(0,len(num)):

		if( prev == num[i]):
			return True
		prev = num[i]
		