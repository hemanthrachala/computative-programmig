# A happy prime is a number that is both happy and prime. 
# Write the function nthHappyPrime(n) which takes a non-negative integer 
# and returns the nth happy prime number (where the 0th happy prime number is 7).


def isHappyNumber(n):

	def squares_sum(num):
		sum = 0

		while ( num > 0):
			rem = num % 10
			sum = sum + (rem*rem)
			num = num // 10
		return sum
	l = []

	while squares_sum(n) not in l:
		res = squares_sum(n)
		if res == 1:
			return True
		else:
			l.append(res)
			n = res			 
	else:
		return False

def is_prime(num):
	if num >= 1 :
		for i in range(2,num):
			if (num % i == 0):
				return False
		return True
	else:
		return False			


def fun_nth_happy_prime(n):
	
	l = [i for i in range(100) if (isHappyNumber(i) and is_prime(i))]
	return l.__getitem__(n)