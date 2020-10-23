# https://leetcode.com/problems/squares-of-a-sorted-array/
class Solution:
    def sortedSquares(self, a: List[int]) -> List[int]:
        if len(a) != 0:
            a = sorted(a, key = lambda x: abs(x))
            for i in range(len(a)):
                a[i] = a[i] * a[i]
        return a