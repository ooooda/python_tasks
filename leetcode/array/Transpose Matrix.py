# https://leetcode.com/problems/transpose-matrix/
class Solution:
    def transpose(self, a: List[List[int]]) -> List[List[int]]:
        if len(a) == 0:
            return a
        c = 0
        i = 0
        j = 0
        helper = []
        for _ in a:
            c += 1
        r = len(a[0])
        res = []
        while i != r:
            if j != c:
                helper.append(a[j][i])
                j += 1
            else:
                j = 0
                res.append(helper)
                helper = []
                i += 1
        return res