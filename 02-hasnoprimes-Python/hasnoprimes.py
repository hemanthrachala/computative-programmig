# Write the function hasnoprimes(L) that takes a 2d list L of integers, 
# and returns True if L does not contain any primes, and False otherwise.


def is_prime(n):
	if n > 1:
		for i in range(2,n):
			if(n%i == 0):
				return False
			return True
	return False		
def fun_hasnoprimes(l):
	lst = [j for i in l for j in i]
	lsts = list(set(lst))

	for i in lsts:
		if (is_prime(int(i))):
			return False
		return True	


