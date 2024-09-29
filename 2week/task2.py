"""
leetcode.com/problem-list/string/
url: https://leetcode.com/problems/longest-palindromic-substring/
"""


class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""

        def getMaxPal(l, r, s):
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1

            return s[l + 1:r]

        for i in range(len(s)):
            first = getMaxPal(i, i, s)
            second = getMaxPal(i, i + 1, s)

            if len(first) > len(second) and len(first) > len(res):
                res = first
            elif len(second) > len(res):
                res = second

        return res