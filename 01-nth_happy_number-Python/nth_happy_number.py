# Write the function nthHappyNumber(n) which takes a non-negative integer 
# and returns the nth happy number (where the 0th happy number is 1). 
# Here are some test assertions for you:
# assert(nthHappyNumber(0) == 1)
# assert(nthHappyNumber(1) == 7)
# assert(nthHappyNumber(2) == 10)
# assert(nthHappyNumber(3) == 13)
# assert(nthHappyNumber(4) == 19)
# assert(nthHappyNumber(5) == 23)
# assert(nthHappyNumber(6) == 28)
# assert(nthHappyNumber(7) == 31)


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
		res = squares_sum(res)
		if res == 1:
			return True
		else:
			l.append(res)
			n = res			 



def fun_nth_happy_number(n):
	
	happynum = [i for i in range(10) if isHappyNumber(i)]
	return happynum[n]
