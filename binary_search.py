def binary_search_rec(input_array, value, index):
    if len(input_array) == 1:
        return -1
    half = int(len(input_array)/2)
    if value == input_array[half]:
        return index+half
    if value > input_array[half]:
        return binary_search_rec(input_array[half:], value, index+half)
    if value < input_array[half]:
        return binary_search_rec(input_array[:half], value, index)

def binary_search(input_array, value):
    """Your code goes here."""
    half = int(len(input_array)/2)
    if value == input_array[half]:
        return half
    if value > input_array[half]:
        return binary_search_rec(input_array[half:], value, half)
    if value < input_array[half]:
        return binary_search_rec(input_array[:half], value, 0)

test_list = [1,3,9,11,15,19,29]
test_val1 = 25
test_val2 = 15
print(binary_search(test_list, test_val1))
print(binary_search(test_list, test_val2))