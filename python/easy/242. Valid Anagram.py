"""
Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase,
typically using all the original letters exactly once.

Example 1:
Input: s = "anagram", t = "nagaram"
Output: true

Example 2:
Input: s = "rat", t = "car"
Output: false

Constraints:
1 <= s.length, t.length <= 5 * 104
s and t consist of lowercase English letters.
"""


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        dict_s = {}
        dict_t = {}
        for char_s, char_t in zip(s, t):
            dict_s[char_s] = dict_s.get(char_s, 0) + 1
            dict_t[char_t] = dict_t.get(char_t, 0) + 1
        return dict_s == dict_t


s = Solution()
print(s.isAnagram(s="anagram", t="nagaram"))
print(s.isAnagram(s="rat", t="car"))
