""" Given a list, find the k-th largest element in the list.
Input: list = [3, 5, 2, 4, 6, 8], k = 3
Output: 5
Here is a starting point:
"""


def findKthLargest(nums, k):
    if k > len(nums) or k - 1 < 0:
        return -1
    else:
        sort = sorted(nums)[::-1]
        return sort[k - 1]


print(findKthLargest([3, 5, 2, 4, 6, 8], 1))
# 5
