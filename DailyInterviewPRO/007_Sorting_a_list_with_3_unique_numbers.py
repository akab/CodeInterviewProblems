""" Given a list of numbers with only 3 unique numbers (1, 2, 3), sort the list in O(n) time. 

Example 1:
Input: [3, 3, 2, 1, 3, 2, 1]
Output: [1, 1, 2, 2, 3, 3, 3]

Challenge: Try sorting the list using constant space.
"""
import time


def sortNumsMergeSort(nums):
    if len(nums) > 1:
        m = len(nums) // 2
        left = nums[:m]
        right = nums[m:]
        left = sortNumsMergeSort(left)
        right = sortNumsMergeSort(right)

        nums = []

        while len(left) > 0 and len(right) > 0:
            if left[0] < right[0]:
                nums.append(left[0])
                left.pop(0)
            else:
                nums.append(right[0])
                right.pop(0)

        for i in left:
            nums.append(i)
        for i in right:
            nums.append(i)

    return nums


def sortNums(nums):
    # Fill this in.
    ones = []
    twos = []
    threes = []
    for n in nums:
        if n == 1:
            ones.append(n)
        elif n == 2:
            twos.append(n)
        else:
            threes.append(n)

    return ones + twos + threes


arr = [3, 3, 2, 1, 3, 2, 1]
start = time.time()
print(sortNums(arr))
print("sortNums() time:", time.time() - start)
start = time.time()
print(sortNumsMergeSort(arr))
print("sortNumsMergeSort() time:", time.time() - start)
# [1, 1, 2, 2, 3, 3, 3]
