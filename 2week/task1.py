"""
leetcode.com/problem-list/string/
url: https://leetcode.com/problems/reverse-words-in-a-string/
"""


class Solution:
    def reverseWords(self, s: str) -> str:
        current = ""
        res = ""

        for i in range(len(s) - 1, -1, -1):
            if s[i] != " ":
                current += s[i]
            elif current != "":
                res += current[::-1]
                current = ""
                res += " "

            if i == 0:
                res += current[::-1]

        if current == "":
            res = res[:-1]

        return res