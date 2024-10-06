"""
https://leetcode.com/problem-list/array/
url: https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/
"""


class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        left = 0
        right = len(nums) - 1

        if len(nums) == 0:
            return [-1, -1]

        while right - left > 1:
            pos = round((left + right) / 2)
            if target < nums[pos]:
                right = pos
            elif target > nums[pos]:
                left = pos
            else:
                left = pos
                right = pos

                while left >= 0 and nums[left] == target:
                    left -= 1
                while right < len(nums) and nums[right] == target:
                    right += 1

                return [left + 1, right - 1]

        if nums[left] == target and nums[right] == target:
            return [left, right]
        elif nums[left] == target:
            return [left, left]
        elif nums[right] == target:
            return [right, right]

        return [-1, -1]
