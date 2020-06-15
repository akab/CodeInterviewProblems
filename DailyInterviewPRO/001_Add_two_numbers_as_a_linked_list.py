""" You are given two linked-lists representing two non-negative integers. 
The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

Example:
Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.
"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def addTwoNumbers(self, l1, l2, c=0):
        # Fill this in.
        prev = None
        curr = None
        head = None
        carry = 0
        while l1 is not None or l2 is not None:
            if l1 is None:
                value1 = 0
            else:
                value1 = l1.val
            if l2 is None:
                value2 = 0
            else:
                value2 = l2.val

            _sum = value1 + value2 + carry
            carry = 1 if _sum >= 10 else 0
            _sum = _sum if _sum < 10 else _sum % 10

            curr = ListNode(_sum)

            if head is None:
                head = curr
            else:
                prev.next = curr

            prev = curr

            if l1 is not None:
                l1 = l1.next
            if l2 is not None:
                l2 = l2.next

        if carry > 0:
            curr.next = ListNode(carry)

        return head


l1 = ListNode(2)
l1.next = ListNode(4)
l1.next.next = ListNode(3)

l2 = ListNode(5)
l2.next = ListNode(6)
l2.next.next = ListNode(4)

result = Solution().addTwoNumbers(l1, l2)
while result:
    print(result.val),
    result = result.next
# 7 0 8
