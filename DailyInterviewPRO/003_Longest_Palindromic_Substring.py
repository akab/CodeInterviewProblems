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
      # TODO use two indices to scan the string
      """
      idx1 = 0
      idx2 = len(s)-1
      output = ''
      while idx1 != idx2:
      	if s[idx1] == [idx2]:
      		while s[idx1] == [idx2]:
      			idx1 += 1
      			idx2 -= 1
      """

        
# Test program
s = "tracecars"
print(str(Solution().longestPalindrome(s)))
# racecar
