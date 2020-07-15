# isrighttriangle(x1, y1, x2, y2, x3, y3)[5pts]
# Write the function isrighttriangle(x1, y1, x2, y2, x3, y3) that takes 6 int or float values that
# represent the vertices (x1,y1), (x2,y2), and (x3,y3) of a triangle, and returns True if that is
# a right triangle and False otherwise. You may wish to write a helper function,
# distance(x1, y1, x2, y2), which you might call several times. Also, remember to use
# almostEqual (instead of ==) when comparing floats.
import math
def isrighttriangle(x1, y1, x2, y2, x3, y3):
	# your code goes here
	l = distance(x1,y1,x2,y2)
	m = distance(x2,y2,x3,y3)
	n = distance(x1,y1,x3,y3)

	maximum = max(l,m,n)

	if(maximum == l and math.isclose(l*l,(m*m + n*n))):
		return True
	if(maximum == m and math.isclose(m*m,(l*l + n*n))):
		return True
	if(maximum == n and math.isclose(n*n,(l*l + m*m))):
		return True	
	else:
		return False		
	
def distance(x1,y1,x2,y2):

	dist = math.sqrt((x1-x2)**2 + (y1-y2)**2)
	return dist	
