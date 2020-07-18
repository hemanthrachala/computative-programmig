# median(a) (10 pts)
# Write the non-destructive function median(a) that takes a list of ints or floats and returns the median value, 
# which is the value of the middle element, or the average of the two middle elements if there is no single middle 
# element. If the list is empty, return None.

def median(a):
	# your code goes here
	length = len(a)

	a.sort()

	if length == 1:
		return a[0]

	if length % 2 == 0:
		m1 = a[length//2]
		m2 = a[length//2 -1]
		m = (m1+m2)/2
	else:
		m = a[length//2]

	return m	