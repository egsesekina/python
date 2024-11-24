"""
https://leetcode.com/problem-list/sliding-window/
url: https://leetcode.com/problems/number-of-sub-arrays-of-size-k-and-average-greater-than-or-equal-to-threshold/
"""


class Solution:
    def numOfSubarrays(self, arr: list[int], k: int, threshold: int) -> int:
        s = sum(arr[:k])
        cnt = 0
        if s / k >= threshold:
            cnt += 1
        for i in range(k, len(arr)):
            s += arr[i]
            s -= arr[i - k]
            if s / k >= threshold:
                cnt += 1
        return cnt
