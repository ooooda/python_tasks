# https://leetcode.com/problems/image-smoother/
from copy import deepcopy

class Solution:
    def imageSmoother(self, a: List[List[int]]) -> List[List[int]]:
        if len(a) == 0:
            return a
        res = deepcopy(a)
        for i, el in enumerate(a):
            for j, elem in enumerate(el):
                s = elem
                cnt = 1
                if i != 0:
                    s += a[i - 1][j]
                    cnt += 1
                    if j != 0:
                        s += a[i - 1][j - 1]
                        cnt += 1
                    if j != len(el) - 1:
                        s += a[i - 1][j + 1]
                        cnt += 1
                if j != 0:
                    s += a[i][j - 1]
                    cnt += 1
                if j != len(el) - 1:
                    s += a[i][j + 1]
                    cnt += 1
                if i != len(a) - 1:
                    s += a[i + 1][j]
                    cnt += 1
                    if j != 0:
                        s += a[i + 1][j - 1]
                        cnt += 1
                    if j != len(el) - 1:
                        s += a[i + 1][j + 1]
                        cnt += 1
                res[i][j] = s // cnt
        return res

