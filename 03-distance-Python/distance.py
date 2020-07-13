# Write the function fun_distance(x1, y1, x2, y2) 
# that takes four int values x1, y1, x2, y2 
# that represent the two points (x1, y1) and (x2, y2), 
# and returns the distance between those points as a int.
import math
# we can do it in two ways 
#1.   y1-y1//x2-x1
#2. sqrt of (y2-y1)2 + (x2-x1)2

def fun_distance(x1, y1, x2, y2):
	# your code goes here

	distance = math.sqrt((x2-x1)**2 + (y2-y1)**2)

	return distance