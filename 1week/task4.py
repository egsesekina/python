"""
leetcode.com/problem-list/string/
url: https://leetcode.com/problems/edit-distance/
"""


class Solution(object):
    def minDistance(self, word1, word2):
        arr = [[0 for _ in range(len(word1)+1)] for _ in range(len(word2)+1)]

        c = 0
        for x in range (len(word1)+1):
            arr[0][x] = c
            c+=1

        c = 0
        for x in range (len(word2)+1):
            arr[x][0] = c
            c+=1

        for x in range (1, len(word2)+1):
            for y in range (1, len(word1)+1):
                if (word2[x-1] == word1[y-1]): arr[x][y] = min(arr[x-1][y]+1, arr[x][y-1]+1, arr[x-1][y-1])
                else: arr[x][y] = min(arr[x-1][y]+1, arr[x][y-1]+1, arr[x-1][y-1]+1)

        return(arr[len(word2)][len(word1)])