"""
https://leetcode.com/problem-list/array/
url: https://leetcode.com/problems/container-with-most-water/
"""


class Solution:
    def maxArea(self, height: list[int]) -> int:
        left = 0
        right = len(height) - 1
        maxArea = 0

        while left < right:
            width = right - left
            currentHeight = min(height[left], height[right])

            currentArea = width * currentHeight
            maxArea = max(maxArea, currentArea)

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return maxArea
