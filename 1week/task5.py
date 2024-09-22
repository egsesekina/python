"""
leetcode.com/problem-list/string/
url: https://leetcode.com/problems/largest-number/description/
"""


class Solution(object):
    def largestNumber(self, nums):
        res = ""
        i = 0

        while i != len(nums):
            j = i + 1
            while j != len(nums):
                if (int(str(nums[i]) + str(nums[j])) < int(str(nums[j]) + str(nums[i]))):
                    nums[i], nums[j] = nums[j], nums[i]
                j += 1
            i += 1

        for i in nums:
            res += str(i)

        if (res[0] == '0'): return "0"

        return res
