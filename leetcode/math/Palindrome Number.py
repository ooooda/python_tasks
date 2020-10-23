# https://leetcode.com/problems/palindrome-number/
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 or (x != 0 and x % 10 == 0):
            return False
        if 0 <= x <= 9:
            return True
        helper = x
        skip = 0
        cnt = 0
        while helper > 0:
            helper //= 10
            cnt += 1
        if cnt % 2 != 0:
            skip = 1
        cnt //= 2
        x1 = x // (10 ** (cnt + skip))
        x2 = x % (10 ** cnt)
        for i in range(1, cnt + 1):
            if x1 // (10 ** (cnt - 1)) != x2 % 10:
                return False
            x1 %= 10 ** (cnt - 1)
            x2 = (x2 - x2 % 10) // 10
            cnt -= 1
        return True