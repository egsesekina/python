"""
https://leetcode.com/problem-list/sliding-window/
url: https://leetcode.com/problems/arithmetic-slices/
"""


class Solution:
    def numberOfArithmeticSlices(self, nums: list[int]) -> int:
        n = len(nums)
        count = 0

        for i in range(n):
            for j in range(i + 2, n):
                diff = nums[i + 1] - nums[i]
                f = True
                for k in range(i + 1, j):
                    if nums[k + 1] - nums[k] != diff:
                        f = False
                        break
                if f:
                    count += 1

        return count
