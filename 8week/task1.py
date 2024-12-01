"""
https://leetcode.com/problem-list/sliding-window/
url: https://leetcode.com/problems/repeated-dna-sequences/
"""


class Solution:
    def findRepeatedDnaSequences(self, s: str) -> list[str]:
        res = set()
        seen = set()
        for i in range(len(s) - 9):
            curr = s[i : i + 10]
            if curr in seen:
                res.add(curr)
            seen.add(curr)
        return list(res)
