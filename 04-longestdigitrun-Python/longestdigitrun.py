# longestDigitRun(n) [20 pts]
# Write the function longestDigitRun(n) that takes a possibly-negative int value n and returns 
# the digit that has the longest consecutive 
# run, or the smallest such digit if there is a tie. So, longestDigitRun(117773732) returns 7 (
# because there is a run of 3 consecutive 7's), 
# as does longestDigitRun(-677886).
def longestdigitrun(n):
	# Your code goes here

	longstrun = 1
	longstdrun = n % 10
	crun = 1
	index = n

	c = 0

	while index != 0:
		index = index // 10
		c += 1

	if c == 1:
		return 1

	for i in range(c):
		temp1 = n % 10
		n = n // 10
		temp2 = n % 10

		if temp1 == temp2:
			crun += 1
		elif crun > longstrun:
			longstrun = crun
			longstdrun = temp1
			crun = 1
		elif crun == longstrun  and temp1 < longstdrun:
			longstdrun = temp1 
			crun = 1
		else:
			crun = 1
	return longstdrun			
