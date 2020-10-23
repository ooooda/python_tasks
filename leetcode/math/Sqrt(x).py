# https://leetcode.com/problems/sqrtx/
class Solution:
    def binary_search(self, x, l, r):
        m = (l + r) // 2
        if m * m <= x:
            if (m + 1) ** 2 > x:
                return m
            else:
                return self.binary_search(x, m, r)
        else:
            return self.binary_search(x, l, m)

    def mySqrt(self, x: int) -> int:
        if x == 0 or x == 1:
            return x
        return self.binary_search(x, 1, x + 1)