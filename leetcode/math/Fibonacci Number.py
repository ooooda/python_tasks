# https://leetcode.com/problems/fibonacci-number/
class Solution:
    def fib(self, n: int) -> int:
        fib = [0, 1]
        if n == len(fib) - 1:
            return fib[n]
        x = n  - len(fib)
        for _ in range(x + 1):
            fib.append(fib[-1] + fib[-2])
        return fib[n]