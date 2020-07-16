# Write the function getKthDigit(n, k) that takes 
# a possibly-negative int n and a non-negative int k, 
# and returns the kth digit of n, starting from 0, counting from the right.
# if the kth digit is not present return 0 



def fun_get_kth_digit(digit, k):
	
	digit = n

	if(n > 1):
		n = str(n)
		if(k < len(n)):
			return int(n[len(n)-k-1])
		else:
			return 0
	else:
		return 0			