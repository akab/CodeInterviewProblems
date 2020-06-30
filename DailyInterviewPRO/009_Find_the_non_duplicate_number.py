""" Given a list of numbers, 
where every number shows up twice except for one number, find that one number.

Example:
Input: [4, 3, 2, 4, 1, 3, 2]
Output: 1

Challenge: Find a way to do this using O(1) memory.
"""


def singleNumber(nums):
    nums.sort()
    res = None
    for index, x in enumerate(nums[:-1:2]):
        if nums[index + 1] != x:
            res = x
    return res


print(singleNumber([4, 3, 2, 4, 1, 3, 2]))
# print(singleNumber([4, 3, 2, 4, 1, 3, 2]))
# 1
