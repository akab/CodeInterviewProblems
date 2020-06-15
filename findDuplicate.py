""" Find the duplicate number in a finite number series """
""" Requirements:  O(n) time and O(1) space	"""
""" Solution: See https://en.wikipedia.org/wiki/Cycle_detection """

import time


def findDuplicate(nums):
    tortoise = nums[0]
    hare = nums[0]
    while True:
        tortoise = nums[tortoise]
        hare = nums[nums[hare]]
        if tortoise == hare:
            break

    ptr1 = nums[0]
    ptr2 = tortoise
    while ptr1 != ptr2:
        ptr1 = nums[ptr1]
        ptr2 = nums[ptr2]

    return ptr1


start_time = time.time()
print("duplicate is: ", findDuplicate([1, 2, 4, 3, 1]))
print("elapsed time: %f" % (time.time() - start_time))
