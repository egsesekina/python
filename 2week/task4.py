"""
leetcode.com/problem-list/string/
url: https://leetcode.com/problems/zigzag-conversion/
"""


class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s

        rows = ["" for _ in range(numRows)]
        res = ""

        i = 0
        diag = 0

        for ch in s:
            rows[i] += ch
            if (i == numRows - 1): diag = 1
            if (i == 0): diag = 0

            if (diag == 0): i+=1
            else: i-=1

        for r in rows:
            res+=r

        return res