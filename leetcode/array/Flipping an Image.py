# https://leetcode.com/problems/flipping-an-image/
class Solution:
    def flipAndInvertImage(self, a: List[List[int]]) -> List[List[int]]:
        for i, el in enumerate(a):
            a[i] = el[::-1]
        for i in range(len(a)):
            for j in range(len(a[i])):
                if a[i][j] == 1:
                    a[i][j] = 0
                    continue
                else:
                    a[i][j] = 1
                    continue
        return a