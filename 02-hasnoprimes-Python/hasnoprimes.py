# Write the function hasnoprimes(L) that takes a 2d list L of integers, 
# and returns True if L does not contain any primes, and False otherwise.


def is_prime(n):
	pass

def fun_hasnoprimes(l):
	lst = [j for i in l for j in i]
	lst = list(set(lst))

	for i in lst:
		if (is_prime(i)):
			return False
	else:
		return True			


