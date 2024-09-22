"""
leetcode.com/problem-list/string/
url: https://leetcode.com/problems/letter-combinations-of-a-phone-number/description/
"""


class Solution:
    def letterCombinations(self, digits):
        if  len(digits)==0: return []
        res = [""]

        dictionary = {
            2: "abc",
            3: "def",
            4: "ghi",
            5: "jkl",
            6: "mno",
            7: "pqrs",
            8: "tuv",
            9: "wxyz"
        }

        for d in digits:
            tmp = []
            for letter in dictionary[int(d)]:
                for r in res:
                    tmp.append(r+letter)
            res = tmp

        return res