"""
https://leetcode.com/problem-list/array/
url: https://leetcode.com/problems/jump-game/
"""


class Solution:
    def canJump(self, nums: list[int]) -> bool:
        maxReachable = 0
        for i in range(len(nums)):
            if i > maxReachable:
                return False
            maxReachable = max(maxReachable, i + nums[i])
        return True
