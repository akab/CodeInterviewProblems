""" A palindrome is a sequence of characters that reads the same backwards and forwards. 
Given a string, s, find the longest palindromic substring in s.

Example: 
Input: "banana"
Output: "anana"

Input: "million"
Output: "illi"
"""


class Solution:
    def longestPalindrome(self, s):
        idx1 = 0
        idx2 = len(s) - 1
        front = ''
        back = ''
        while idx1 != idx2 and idx1 < len(s) and idx2 > 0:
            if s[idx1] == s[idx2]:
                front += s[idx1]
                back += s[idx2]
            # TODO find better way to handle indices
            idx1 += 1
            idx2 -= 1
        front += s[idx1]
        return front + back[::-1]


# Test program
#s = "tracecars"
s = "banana"
print(str(Solution().longestPalindrome(s)))
# racecar
