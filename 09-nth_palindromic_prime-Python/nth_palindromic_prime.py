# Write the function fun_nth_palindromic_prime(n) that takes a non-negative int n 
# and returns the nth palindromic Prime, which is a palidrome number such that 
# it is also a prime. For example, 313 is a palindrome and it is prime 
# so 313 is an palindrome Prime. fun_nth_palindrome_prime(0) returns 2


def is_prime(num) :

	if num > 1:
		for i in range(2,num):
			if num % i == 0:
				return False
			else:
				return True	


def fun_nth_palindromic_prime(n):
	return 0