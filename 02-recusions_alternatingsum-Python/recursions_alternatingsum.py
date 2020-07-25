# Write the function alternatingSum(L) that takes a possibly-empty list of numbers, 
# and returns the alternating sum of the list, where every other value is subtracted 
# rather than added. For example: alternatingSum([1,2,3,4,5]) returns 1-2+3-4+5 
# (that is, 3). If L is empty, return 0. You may not use loops/iteration in this problem.

def fun(l,flag):
	if len(l) == 0:
		return 0
	else:
		if flag:

			return l[0] + fun(l[1:], False)	
		else:
			return -l[0] + fun(l[1:], True)

def fun_recursions_alternatingsum(l): 
	flag = True
	return fun(l, flag)