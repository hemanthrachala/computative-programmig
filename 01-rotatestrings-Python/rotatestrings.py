# Write the function rotatestring(s, k) that takes a string s and a possibly-negative integer k. 
# If k is non-negative, the function returns the string s rotated k places to the left. 
# If k is negative, the function returns the string s rotated |k| places to the right. So, for example:
# assert(rotateString('abcd',  1) == 'bcda')
# assert(rotateString('abcd', -1) == 'dabc')



def fun_rotatestrings(s, n):
	new = ""
	if n > 0:
		n = n % len(s)
		new = s[n:] + s[:n]
		return new
	if n < 0:
		n = abs(n)
		n = n % len(s)
		new = s[len(s)-n:] + s[:len(s)-n]
		return new
	else:
		return s	
