"""
Given an integer x, return true if x is a palindrome, and false otherwise.

Example 1:
Input: x = 121
Output: true
Explanation: 121 reads as 121 from left to right and from right to left.

Example 2:
Input: x = -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.

Example 3:
Input: x = 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
"""


class Solution:
    # My solution
    def isPalindrome1(self, x: int) -> bool:
        if x < 0:
            return False

        return str(x) == str(x)[::-1]

    # without converting the input to string
    def isPalindrome2(self, x: int) -> bool:
        if x < 0:
            return False

        input_num = x
        new_num = 0
        while x > 0:
            new_num = new_num * 10 + x % 10
            x = x // 10
        return new_num == input_num

    # 99.14% faster
    def isPalindrome3(self, x: int) -> bool:
        # if x is negative. if x is positive and last digit is 0, that also cannot form a palindrome
        if x < 0 or (x > 0 and x % 10 == 0):
            return False

        result = 0
        while x > result:
            result = result * 10 + x % 10
            x = x // 10

        return True if (x == result or x == result // 10) else False


s = Solution()
res1 = s.isPalindrome1(151)
print(res1)

res2 = s.isPalindrome2(152)
print(res2)

res3 = s.isPalindrome3(15251)
print(res3)
