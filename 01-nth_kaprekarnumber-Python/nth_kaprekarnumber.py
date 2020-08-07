# Background: a Kaprekar number is a non-negative integer, the representation of whose square 
# can be split into two possibly-different-length parts (where the right part is not zero) 
# that add up to the original number again. For instance, 45 is a Kaprekar number, because 
# 45**2 = 2025 and 20+25 = 45. You can read more about Kaprekar numbers here. The first several 
# Kaprekar numbers are: 1, 9, 45, 55, 99, 297, 703, 999 , 2223, 2728,... 
# With this in mind, write the function nthKaprekarNumber(n) that takes a non-negative int n 
# and returns the nth Kaprekar number, where as usual we start counting at n==0.


import math


def iskasperkar(num):
    if num <=0:
        return False
    sqr = num ** 2
    if sqr < 10:
        if sqr == num:
            return True

    numm = math.ceil(math.log(sqr,10))
    c = 1
    while c < numm:
        num1 = sqr % 10 ** c
        num2 = sqr // 10 ** c

        if num1 == 0:
            c +=1
            continue
        if num1 + num2 == num:
            return True
            
        c += 1
    return False        

def fun_nth_kaprekarnumber(n):
    list = []
    for i in range(100000):
        if iskasperkar(i):
            list.append(i)
    return list[n]        
