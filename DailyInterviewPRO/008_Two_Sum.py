"""
You are given a list of numbers, and a target number k.
Return whether or not there are two numbers in the list that add up to k.

Example:
Given [4, 7, 1 , -3, 2] and k = 5, 
return true since 4 + 1 = 5.

Try to do it in a single pass of the list.
"""


def two_sum(nums, k):
    seen = set()
    for num in nums:
        diff = k - num
        if diff in seen:
            return True
        seen.add(num)
    return False


def two_sum_brute(list, k):
    for idx in range(len(list)):
        num = list[idx]
        for idx2 in range(len(list)):
            if idx2 == idx:
                continue
            num2 = list[idx2]
            if num + num2 == k:
                return True
    return False


print(two_sum([4, 7, 1, -3, 2], 8))
# True
