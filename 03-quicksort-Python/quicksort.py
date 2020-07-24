"""Implement quick sort in Python.
Input a list.
Output a sorted list."""
def quicksort(array):
	# Your code goes here
	arr = array

	low = []
	same =[]
	high = []

	if len(arr) > 1:
		pi = arr[0]
		for i in arr:
			if i < pi:
				low.append(i)
			elif i == pi:
				same.append(i)	
			elif i > pi:
				high.append(i)	
		return low + high

	else:
		return arr					