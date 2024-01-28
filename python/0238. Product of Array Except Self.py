"""
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].
The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
You must write an algorithm that runs in O(n) time and without using the division operation.

Example 1:
Input: nums = [1,2,3,4]
Output: [24,12,8,6]

Example 2:
Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]
"""


class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        res = [1] * len(nums)

        pref = 1
        for idx, num in enumerate(nums):
            res[idx] = pref
            pref *= num

        suff = 1
        for idx in range(len(nums) - 1, -1, -1):
            res[idx] *= suff
            suff *= nums[idx]

        return res


s = Solution()
res = s.productExceptSelf([1, 2, 3, 4])
print(res)
res = s.productExceptSelf([-1, 1, 0, -3, 3])
print(res)
