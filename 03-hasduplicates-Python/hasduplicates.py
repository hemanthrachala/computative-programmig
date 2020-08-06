# hasDuplicates(L) [15 pts]
# Write the function hasDuplicates(L) that takes a 2d list L of arbitrary values, and returns True if L 
# contains any duplicate values (that is, 
# if any two values in L are equal to each other), and False otherwise.

def hasduplicates(L):
	# Your code goes here
	lst = [ j for sub in L for j in sub]
	lsts = list(set(lst))

	if len(lst) == len(lsts):
		return True
	return False	