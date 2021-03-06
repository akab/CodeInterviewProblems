"""Implement quick sort in Python.
Input a list.
Output a sorted list."""
def partition(array, low, high):
    i = (low-1)
    pivot = array[high]
    
    for j in range(low, high):
        if pivot >= array[j]:
            i += 1
            array[i], array[j] = array[j], array[i]
            
    array[i+1],array[high] = array[high],array[i+1] 
    return ( i+1 )


def quicksort_rec(array, low, high):
    if low < high:
        pi = partition(array, low, high)
        
        quicksort_rec(array, low, pi-1)
        quicksort_rec(array, pi+1, high)
    
    

def quicksort(array):
    quicksort_rec(array, 0, len(array)-1)
    return array

test = [21, 4, 1, 3, 9, 20, 25, 6, 21, 14]
print quicksort(test)