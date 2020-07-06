""" Imagine you are building a compiler.
Before running any code, the compiler must check that the parentheses in the program are balanced.
Every opening bracket must have a corresponding closing bracket. We can approximate this using strings. 

Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid. 
An input string is valid if:
- Open brackets are closed by the same type of brackets.
- Open brackets are closed in the correct order.
- Note that an empty string is also considered valid.

Example:
Input: "((()))"
Output: True

Input: "[()]{}"
Output: True

Input: "({[)]"
Output: False
"""


class Solution:
    def isValid(self, s):
        if s == "":
            return True

        round = 0
        square = 0
        curly = 0
        for c in s:
            if c == '(':
                round += 1
            if c == ')':
                round -= 1
            if c == '[':
                square += 1
            if c == ']':
                square -= 1
            if c == '{':
                curly += 1
            if c == '}':
                curly -= 1

        return round == square == curly == 0


# Test Program
s = "()(){(())"
# should return False
print(Solution().isValid(s))

s = ""
# should return True
print(Solution().isValid(s))

s = "([{}])()"
# should return True
print(Solution().isValid(s))

s = "((()))"
# should return True
print(Solution().isValid(s))

s = "[()]{}"
# should return True
print(Solution().isValid(s))

s = "({[)]"
# should return False
print(Solution().isValid(s))
