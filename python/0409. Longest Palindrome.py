class Solution:
    def longestPalindrome(self, s: str) -> int:
        cach = {}

        for c in s:
            cach[c] = cach.get(c, 0) + 1

        max_length = 0
        for k, v in cach.items():
            k_len = v // 2
            max_length += 2 * k_len

        return max_length if max_length == len(s) else max_length + 1


s = Solution()
res = s.longestPalindrome("ababababa")
print(res)
assert res == 9
