"""
https://leetcode.com/problem-list/sliding-window/
url: https://leetcode.com/problems/minimum-number-of-flips-to-make-the-binary-string-alternating/
"""


class Solution:
    def minFlips(self, s: str) -> int:
        cnt0 = s[::2].count("0") + s[1::2].count("1")
        cnt1 = len(s) - cnt0
        ans = min(cnt0, cnt1)
        if not len(s) % 2:
            return ans
        for n in s:
            cnt0, cnt1 = cnt1, cnt0
            if n == "1":
                cnt1 += 1
                cnt0 -= 1
            else:
                cnt0 += 1
                cnt1 -= 1
            ans = min(cnt0, cnt1, ans)
        return ans
url: https://leetcode.com/problems/longest-substring-without-repeating-characters/
"""


class Solution:
    def lengthOfLongestSubstring(self, s):
        res = 0

        currentstart = 0
        currentword = set()

        for letter in s:
            while letter in currentword:
                currentword.remove(s[currentstart])
                currentstart += 1

            currentword.add(letter)
            res = max(res, len(currentword))

        return res
