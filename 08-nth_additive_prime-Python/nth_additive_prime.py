# Write the function fun_nth_additive_prime(n) that takes a non-negative int n 
# and returns the nth Additive Prime, which is a prime number such that 
# the sum of its digits is also prime. For example, 113 is prime and 1+1+3==5 and 5 
# is also prime, so 113 is an Additive Prime. fun_nth_additive_prime(0) returns 2


def is_prime(num):
	if num > 1:
		for i in range(2,num):
			if(num % i == 0):
				return False
		return True
	else:
		return True				


def fun_nth_additive_prime(n):
	l = [i  for i in range(50) if is_prime(i)]
	return l[n]