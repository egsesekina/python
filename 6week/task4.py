"""
https://leetcode.com/problem-list/sliding-window/
url: https://leetcode.com/problems/count-number-of-nice-subarrays/
"""


class Solution:
    def numberOfSubarrays(self, nums: list[int], k: int) -> int:
        arr = [0] * (len(nums) + 1)
        arr[0] = 1
        ans, odd_number = 0, 0

        for elem in nums:
            odd_number += elem % 2
            if (odd_number - k) >= 0:
                ans += arr[odd_number - k]
            arr[odd_number] += 1
        return ans
