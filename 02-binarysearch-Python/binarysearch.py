"""You're going to write a binary search function.
You should use an iterative approach - meaning
using loops.
Your function should take two inputs:
a Python list to search through, and the value
you're searching for.
Assume the list only has distinct elements,
meaning there are no repeated values, and 
elements are in a strictly increasing order.
Return the index of value, or -1 if the value
doesn't exist in the list."""

def binary_search(input_array, value):
    # Your code goes here
    arr = input_array
    num = value

    low = 0
    high = len(arr)-1

    while low <= high:
        middle = (low + high ) // 2
        if arr[middle] == num :
            return middle
        elif arr[middle] < num:
            low = middle + 1
        elif arr[middle] > num:
            high = middle - 1
    else:
        return -1                 

