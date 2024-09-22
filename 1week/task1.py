"""
leetcode.com/problem-list/string/
url: https://leetcode.com/problems/longest-substring-without-repeating-characters/description/
"""


class Solution:
    def lengthOfLongestSubstring(self, s):
        res = 0

        currentstart = 0
        currentword = set()

        for letter in s:
            while (letter in currentword):
                currentword.remove(s[currentstart])
                currentstart += 1

            currentword.add(letter)
            res = max(res, len(currentword))

        return res
