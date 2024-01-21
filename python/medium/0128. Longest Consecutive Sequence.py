"""
Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.
You must write an algorithm that runs in O(n) time.

Example 1:
Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.

Example 2:
Input: nums = [0,3,7,2,5,8,4,6,0,1]
Output: 9
"""


class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        nums_set = set(nums)  # O(n)
        max_length = 0

        for num in nums_set:
            if (num - 1) not in nums_set:
                sequence_length = 1
                while (num + sequence_length) in nums_set:
                    sequence_length += 1
                max_length = max(max_length, sequence_length)

        return max_length


s = Solution()
res = s.longestConsecutive([100, 4, 200, 1, 3, 2])
print(res)
res = s.longestConsecutive([0, 3, 7, 2, 5, 8, 4, 6, 0, 1])
print(res)
