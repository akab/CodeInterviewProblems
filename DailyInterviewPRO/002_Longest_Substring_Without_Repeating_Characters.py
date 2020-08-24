""" Given a string, find the length of the longest substring without repeating characters. """
class Solution:
  def lengthOfLongestSubstring(self, s):
    # Fill this in.
    last = ''
    count = 0
    candidates = []
    for char in s:
    	if char == last:
    		candidates.append(count)
    		count = 0

    	count += 1
    	last = char

    print(candidates)
    return max(candidates)

print(Solution().lengthOfLongestSubstring('abrkaabcdefghijjxxx'))
# 10
