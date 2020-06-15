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
    """Your code goes here."""
    half = int(len(input_array)/2)
    index = 0
    search_array = []
    if value == input_array[half]:
        return half
    if value > input_array[half]:
        index = half
        search_array = input_array[half:len(input_array)]
    if value < input_array[half]:
        search_array = input_array[0:half]
        
    for i in search_array:
        if i == value:
            return index
        else:
            index+=1

    return -1
    

test_list = [1,3,9,11,15,19,29]
test_val1 = 25
test_val2 = 15
print binary_search(test_list, test_val1)
print binary_search(test_list, test_val2)