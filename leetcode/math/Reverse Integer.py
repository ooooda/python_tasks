# https://leetcode.com/problems/reverse-integer/
class Solution:
    def reverse(self, x: int) -> int:
        nums = []
        res = 0
        sign = 1
        neg = - 2**31
        pos = 2**31 - 1
        if x < 0:
            sign = -1
            x *= -1
        while x > 0:
            nums.append(x % 10)
            x //= 10
        for i, el in enumerate(nums):
            res += sign * el
            if res == 0 and el == 0:
                continue
            if i != len(nums) - 1:
                res *= 10
            if res > pos or res < neg:
                return 0
        return res