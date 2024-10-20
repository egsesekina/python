"""
https://leetcode.com/problem-list/hash-table/
url: https://leetcode.com/problems/set-matrix-zeroes/
"""


class Solution:
    def setZeroes(self, matrix: list[list[int]]) -> None:
        rows = set()
        columns = set()
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    rows.add(i)
                    columns.add(j)
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if i in rows or j in columns:
                    matrix[i][j] = 0
