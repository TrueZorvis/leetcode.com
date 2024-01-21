"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
An input string is valid if:
Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.

Example 1:
Input: s = "()"
Output: true

Example 2:
Input: s = "()[]{}"
Output: true

Example 3:
Input: s = "(]"
Output: false

Constraints:
1 <= s.length <= 10^4
s consists of parentheses only '()[]{}'.
"""


class Solution:
    def isValid(self, string: str) -> bool:
        bracket_dict = {
            ")": "(",
            "]": "[",
            "}": "{"
        }
        stack = []

        for char in string:
            if char not in bracket_dict:
                stack.append(char)
            else:
                if not stack or stack.pop() != bracket_dict[char]:
                    return False

        return not stack


s = Solution()
res = s.isValid("()")
print(res)
assert res == True

res = s.isValid("()[]{}")
print(res)
assert res == True

res = s.isValid("(]")
print(res)
assert res == False

res = s.isValid("]()")
print(res)
assert res == False

res = s.isValid("[]]")
print(res)
assert res == False
