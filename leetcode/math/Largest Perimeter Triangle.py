# https://leetcode.com/problems/largest-perimeter-triangle/
class Solution:
    def largestPerimeter(self, A: List[int]) -> int:
        res = 0
        i = 0
        A.sort(key=lambda x: -x)
        print(A)
        while i + 2 != len(A):
            if A[i] >= A[i + 1] + A[i + 2]:
                i += 1
            else:
                res = A[i] + A[i + 1] + A[i + 2]
                break
        return res


