class Solution:
    def reverseVowels(self, s: str) -> str:
        word = list(s)
        left = 0
        right = len(word) - 1

        while left < right:
            while word[left].lower() not in ('a', 'e', 'i', 'o', 'u') and left < right:
                left += 1

            while word[right].lower() not in ('a', 'e', 'i', 'o', 'u') and right > left:
                right -= 1

            word[left], word[right] = word[right], word[left]
            left += 1
            right -= 1

        return ''.join(word)


s = Solution()
res = s.reverseVowels('Hello')
print(res)
