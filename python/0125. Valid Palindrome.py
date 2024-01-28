"""
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all
non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.
Given a string s, return true if it is a palindrome, or false otherwise.

Example 1:
Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.

Example 2:
Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.

Example 3:
Input: s = " "
Output: true
Explanation: s is an empty string "" after removing non-alphanumeric characters.
Since an empty string reads the same forward and backward, it is a palindrome.
"""

from string import ascii_lowercase, digits

class Solution:
    def isPalindrome(self, s: str) -> bool:
        string = ''
        for char in s.replace(' ', '').lower():
            if char in ascii_lowercase + digits:
                string += char

        left = 0
        right = len(string) - 1

        while left < right:
            if string[left] != string[right]:
                return False
            left += 1
            right -= 1

        return True


s = Solution()
assert s.isPalindrome('A man, a plan, a canal: Panama') == True
assert s.isPalindrome('race a car') == False
assert s.isPalindrome(' ') == True
assert s.isPalindrome('0P') == False
