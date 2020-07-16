# Write the function setKthDigit(n, k, d) that takes three integers -- n, k, and d 
# where n is a possibly-negative int, k is a non-negative int, and d is a non-negative 
# single digit (between 0 and 9 inclusive). This function returns the number n with 
# the kth digit replaced with d. Counting starts at 0 and goes right-to-left, 
# so the 0th digit is the rightmost digit. 



def fun_set_kth_digit(n, k, d):

	if(n>0):

		n = str(n)

		if(k < len(n)):
			index= int(len(n) - k - 1)
			num = n[0:index]+str(d)+n[index+1 : len(n)]
			return int(num)
		else:
			num = str(d)+ n
			return int(num)

	elif(n<0):
		n = -1*n
		n = str(n)

		if(k < len(n)):
			index= int(len(n) - k - 1)
			num = n[0:index]+str(d)+n[index+1 : len(n)]
			return int(num)
		else:
			num = str(d)+ n
			num = int(num)
			return num*-1




