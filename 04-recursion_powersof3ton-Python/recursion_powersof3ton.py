# Recursion-Only powersOf3ToN(n) [15 pts]
# Write the function powersOf3ToN(n) that takes a possibly-negative float or int n, and returns a list of the 
# positive powers of 3 up to and including n. As an example, powersOf3ToN(10.5) returns [1, 3, 9]. If no such powers 
# of 3 exist, you should return the empty list. You may not use loops/iteration in this problem. 

def helper(n,c,el):
	if n < 1:
		return el
	else:	
		n = n // 3
		c += 1
		num = 3
		return helper(n,c,el+[num **c])

def recursion_powersof3ton(n):
	# Your code goes here
	if int(n) <= 0:
		return None

	el = []

	c = -1
	return helper(n,c,el)
