# fixMostlyMagicSquare(L) [15 pts]
# In this week's writing session, we wrote isMostlyMagicSquare(L). Here, say we have a mostly magic square L, but 
# then we modify L by changing exactly one value in L so that it no longer is a mostly magic square. For this 
# exercise, we assume we have just such a list L, and your task is to find and fix that change. So, given the list 
# L, return a new list M such that M is the same as L, only with exactly one value changed, and M is a mostly magic 
# square.


def fixmostlymagicsquare(L):
	# Your code goes here
	lst = []
	for i in L:
		c = 0
		c += sum(i)
		lst.append(c)

	if len(lst) != len(set(lst)):
		dif = max(lst) - min(lst)

		maxx = max(lst)
		for i in lst:
			if i == maxx:
				indx = lst.index(max(lst))
		d = L[indx]	

		indx1 = d.index(max(d))		

		d[indx1] = max(d) - dif

		L[indx] = d

		return L